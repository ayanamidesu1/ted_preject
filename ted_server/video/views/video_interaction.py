from rest_framework.views import APIView
from django.db import connection, transaction, DatabaseError
import json
from datetime import datetime
from ..log.log import Logger
from django.shortcuts import render
from django.http import JsonResponse

logger = Logger()


class VideoInteraction(APIView):
    def request_path(self, request):
        request_ip = request.META.get('REMOTE_ADDR', '未知IP')
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f'{request_ip} 在 {now} 访问了 {request.path}'

    def get(self, request):
        # 记录未匹配的GET请求
        logger.warning(self.request_path(request) + str(request.user))
        return render(request, '404.html', status=404)

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode())

            # 用户登录校验
            if not request.user.is_authenticated:
                return JsonResponse({'status': 401, 'msg': '用户未登录'}, status=401)

            user_id = request.user.id
            video_id = data.get('video_id')
            interaction_type = data.get('interaction_type')

            # 参数校验
            if not video_id or not interaction_type:
                return JsonResponse({'status': 400, 'msg': '缺少必要参数'}, status=400)

            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # 数据库事务处理
            with transaction.atomic():
                with connection.cursor() as cursor:
                    if interaction_type == 'like':
                        return self.handle_like(cursor, user_id, video_id, now)
                    elif interaction_type == 'collect':
                        return self.handle_collect(cursor, user_id, video_id, now)
                    else:
                        return JsonResponse({'status': 400, 'msg': '未知的操作类型'}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({'status': 400, 'msg': '请求体格式错误，无法解析JSON'}, status=400)

        except DatabaseError as db_err:
            logger.error(f"数据库错误: {str(db_err)}")
            return JsonResponse({'status': 500, 'msg': '数据库操作失败，请稍后重试'}, status=500)

        except Exception as e:
            logger.error(f"服务器错误: {str(e)}")
            return JsonResponse({'status': 500, 'msg': '服务器内部错误'}, status=500)

    def handle_like(self, cursor, user_id, video_id, now):
        # 处理点赞逻辑
        like_sql = '''SELECT * FROM like_table WHERE user_id = %s AND video_id = %s'''
        cursor.execute(like_sql, [user_id, video_id])
        like_result = cursor.fetchone()

        if like_result:
            # 用户已点赞，执行取消点赞
            delete_like_sql = '''DELETE FROM like_table WHERE user_id = %s AND video_id = %s'''
            cursor.execute(delete_like_sql, [user_id, video_id])
            if cursor.rowcount != 1:
                raise Exception('取消点赞失败，回滚操作')
            return JsonResponse({'status': 200, 'msg': '取消点赞成功'}, status=200)
        else:
            # 用户未点赞，执行点赞操作
            insert_like_sql = '''INSERT INTO like_table (video_id, user_id, like_time) VALUES (%s, %s, %s)'''
            cursor.execute(insert_like_sql, [video_id, user_id, now])
            if cursor.rowcount != 1:
                raise Exception('点赞操作失败，回滚操作')
            return JsonResponse({'status': 200, 'msg': '点赞成功'}, status=200)

    def handle_collect(self, cursor, user_id, video_id, now):
        # 处理收藏逻辑
        collect_sql = '''SELECT * FROM collect_table WHERE user_id = %s AND video_id = %s'''
        cursor.execute(collect_sql, [user_id, video_id])
        collect_result = cursor.fetchone()

        if collect_result:
            # 用户已收藏，执行取消收藏
            delete_collect_sql = '''DELETE FROM collect_table WHERE user_id = %s AND video_id = %s'''
            cursor.execute(delete_collect_sql, [user_id, video_id])
            if cursor.rowcount != 1:
                raise Exception('取消收藏失败，回滚操作')
            return JsonResponse({'status': 200, 'msg': '取消收藏成功'}, status=200)
        else:
            # 用户未收藏，执行收藏操作
            insert_collect_sql = '''INSERT INTO collect_table (video_id, user_id, collect_time) VALUES (%s, %s, %s)'''
            cursor.execute(insert_collect_sql, [video_id, user_id, now])
            if cursor.rowcount != 1:
                raise Exception('收藏操作失败，回滚操作')
            return JsonResponse({'status': 200, 'msg': '收藏成功'}, status=200)
