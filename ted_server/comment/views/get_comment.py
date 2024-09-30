from rest_framework.views import APIView
from django.db import connection
import json
from datetime import datetime
from ..log.log import Logger
from django.shortcuts import render
from django.http import JsonResponse

logger = Logger()


class GetComment(APIView):
    def request_path(self, request):
        request_path = request.path
        request_ip = request.META.get('REMOTE_ADDR', '未知IP')
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f'{request_ip} 在 {now} 访问了 {request_path}'

    def get(self, request):
        logger.warning(self.request_path(request) + str(request.user))
        return render(request, '404.html', status=404)

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode('utf-8'))
            video_id = data.get('video_id', None)
            limit = data.get('limit', 10)
            offset = data.get('offset', 0)

            if video_id:
                sql = '''
                SELECT 
                    auth_user.avatar_path,
                    comment_table.*, 
                    comment_table.id AS comment_id, 
                    video_info.id AS video_id, 
                    auth_user.id AS user_id, 
                    auth_user.username AS username,
                    SUM(CASE WHEN comment_interaction.interaction_type = 'like' THEN 1 ELSE 0 END) AS like_count,  
                    SUM(CASE WHEN comment_interaction.interaction_type = 'not_like' THEN 1 ELSE 0 END) AS not_like_count, 
                    MAX(comment_table.send_time) AS send_time 
                FROM 
                    comment_table 
                LEFT JOIN 
                    video_info ON video_info.id = comment_table.video_id 
                LEFT JOIN 
                    auth_user ON auth_user.id = comment_table.send_user_id 
                LEFT JOIN 
                    comment_interaction ON comment_table.id = comment_interaction.comment_id 
                    AND comment_interaction.comment_type = 'comment'
                WHERE 
                    comment_table.video_id = %s
                GROUP BY 
                    comment_table.id, auth_user.id, video_info.id
                ORDER BY 
                    comment_table.send_time DESC
                LIMIT %s OFFSET %s;
                '''

                with connection.cursor() as cursor:
                    cursor.execute(sql, [video_id, limit, offset])
                    columns = [col[0] for col in cursor.description]
                    result = cursor.fetchall()
                    rows = [dict(zip(columns, row)) for row in result]

                    # 获取评论总数
                    cursor.execute('SELECT COUNT(*) FROM comment_table WHERE video_id = %s', [video_id])
                    total = cursor.fetchone()[0]

                    # 删除不需要的字段
                    rows = {'rows': rows, 'total': total}
                    for row in rows['rows']:
                        row.pop('id', None)
                        row.pop('password', None)
                        row.pop('email', None)

                    return JsonResponse({'status': 200, 'msg': '获取评论成功', 'data': rows}, status=200)

            else:
                logger.warning(self.request_path(request) + f' 参数错误: {data}')
                return JsonResponse({'status': 400, 'msg': '参数错误'}, status=400)

        except json.JSONDecodeError:
            logger.error("JSON解析错误")
            return JsonResponse({'status': 400, 'msg': '请求格式错误'}, status=400)
        except Exception as e:
            logger.error(str(e))
            return JsonResponse({'status': 500, 'msg': '服务器错误'}, status=500)
