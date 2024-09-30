from rest_framework.views import APIView
from django.db import connection, transaction
import json
from datetime import datetime
from ..log.log import Logger
from django.shortcuts import render
from django.http import JsonResponse

logger = Logger()

class InteractionComment(APIView):
    def request_path(self, request):
        request_ip = request.META.get('REMOTE_ADDR', '未知IP')
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f'{request_ip} 在 {now} 访问了 {request.path}'

    def get(self, request):
        logger.warning(self.request_path(request) + str(request.user))
        return render(request, '404.html', status=404)

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode())
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            if not request.user.is_authenticated:
                return JsonResponse({'status': 401, 'msg': '用户未登录'}, status=401)

            user_id = request.user.id
            comment_type = data.get('comment_type')
            if comment_type not in ['comment', 'reply']:
                return JsonResponse({'status': 400, 'msg': '参数错误'}, status=400)

            interaction_type = data.get('interaction_type')
            if interaction_type not in ['like', 'not_like']:
                return JsonResponse({'status': 400, 'msg': '参数错误'}, status=400)

            comment_id = data.get('comment_id')

            if not all([comment_type, interaction_type, comment_id]):
                return JsonResponse({'status': 400, 'msg': '参数不完整'}, status=400)

            with transaction.atomic():  # 开启事务
                with connection.cursor() as cursor:
                    # 查询是否已有交互记录
                    select_sql = '''
                    SELECT * FROM comment_interaction 
                    WHERE user_id=%s AND comment_type=%s AND comment_id=%s
                    '''
                    cursor.execute(select_sql, [user_id, comment_type, comment_id])
                    result = cursor.fetchone()

                    if result:
                        # 将结果转换为字典（基于字段名）
                        columns = [col[0] for col in cursor.description]
                        result_dict = dict(zip(columns, result))

                        current_interaction_type = result_dict['interaction_type']
                        if current_interaction_type == interaction_type:
                            # 如果当前交互类型相同，则取消操作（删除记录）
                            delete_sql = '''
                            DELETE FROM comment_interaction 
                            WHERE user_id=%s AND comment_type=%s AND comment_id=%s
                            '''
                            cursor.execute(delete_sql, [user_id, comment_type, comment_id])
                            if cursor.rowcount != 1:
                                raise Exception("删除操作失败，受影响的行数异常")
                            msg = '操作已取消'
                        else:
                            # 如果交互类型相反，则更新为新交互类型
                            update_sql = '''
                            UPDATE comment_interaction 
                            SET interaction_type=%s, interaction_time=%s
                            WHERE user_id=%s AND comment_type=%s AND comment_id=%s
                            '''
                            cursor.execute(update_sql, [interaction_type, now, user_id, comment_type, comment_id])
                            if cursor.rowcount != 1:
                                raise Exception("更新操作失败，受影响的行数异常")
                            msg = '操作已更新'
                    else:
                        # 插入新的记录
                        insert_sql = '''
                        INSERT INTO comment_interaction 
                        (user_id, comment_id, comment_type, interaction_time, interaction_type) 
                        VALUES (%s, %s, %s, %s, %s)
                        '''
                        cursor.execute(insert_sql, [user_id, comment_id, comment_type, now, interaction_type])
                        if cursor.rowcount != 1:
                            raise Exception("插入操作失败，受影响的行数异常")
                        msg = '操作已成功'

                return JsonResponse({'status': 200, 'msg': msg}, status=200)

        except json.JSONDecodeError:
            logger.error("JSON解析错误")
            return JsonResponse({'status': 400, 'msg': 'JSON格式错误'}, status=400)
        except Exception as e:
            logger.error(str(e))
            return JsonResponse({'status': 500, 'msg': '操作失败，已回滚事务'}, status=500)
