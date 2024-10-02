from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection, transaction
from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from .log.log import Logger

logger = Logger()

class GetAllUserInfo(APIView):
    def request_path(self, request):
        request_path = request.path
        request_ip = request.META.get('REMOTE_ADDR', '未知IP')
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f'{request_ip} 在 {now} 访问了 {request_path}'

    def get(self, request):
        logger.warning(self.request_path(request) + str(request.user))
        return render(request, '404.html', status=404)

    def post(self, request):
        try:
            # 用户未登录
            if not request.user.is_authenticated:
                return JsonResponse({'status': 401, 'msg': '用户未登录'}, status=401)

            user_id = request.user.id

            with connection.cursor() as cursor:
                # 获取用户的所有信息，不显式排除字段
                sql = '''
                SELECT * FROM auth_user WHERE id = %s
                '''
                cursor.execute(sql, (user_id,))
                user_info = cursor.fetchone()

                if not user_info:
                    return JsonResponse({'status': 404, 'msg': '用户不存在'}, status=404)

                # 获取列名
                columns = [column[0] for column in cursor.description]
                user_data = dict(zip(columns, user_info))

                # 删除密码字段
                user_data.pop('password', None)

                # 获取用户收藏的视频
                collected_video_sql = '''
                SELECT video_info.*
                FROM collect_table
                JOIN video_info ON collect_table.video_id = video_info.id
                WHERE collect_table.user_id = %s
                '''
                cursor.execute(collected_video_sql, (user_id,))
                collected_videos = cursor.fetchall()
                video_columns = [column[0] for column in cursor.description]
                collected_video_info = [dict(zip(video_columns, video)) for video in collected_videos]

                # 获取用户发布的视频
                user_video_sql = '''
                SELECT * FROM video_info WHERE author_id = %s
                '''
                cursor.execute(user_video_sql, (user_id,))
                user_videos = cursor.fetchall()
                user_video_info = [dict(zip(video_columns, video)) for video in user_videos]

                # 组合数据
                response_data = {
                    'user_info': user_data,
                    'collected_videos': collected_video_info,
                    'user_videos': user_video_info
                }

            return JsonResponse({'status': 200, 'msg': '获取成功', 'data': response_data}, status=200)

        except Exception as e:
            logger.error(f'服务器错误: {e}')
            return JsonResponse({'status': 500, 'msg': '服务器错误'}, status=500)
