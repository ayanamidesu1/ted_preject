from rest_framework.views import APIView
from django.db import connection
import json
from datetime import datetime
from ..log.log import Logger
from django.shortcuts import render
from django.http import JsonResponse

logger = Logger()

class AddComment(APIView):
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
            if not request.user.is_authenticated:
                return JsonResponse({'status': 401, 'msg': '用户未登录'}, status=401)

            user_id = request.user.id
            comment_type = data.get('comment_type')
            comment_content = data.get('comment_content')
            comment_id = data.get('comment_id')
            video_id = data.get('video_id')

            # 校验输入
            if comment_type not in ['comment', 'reply']:
                return JsonResponse({'status': 400, 'msg': '评论类型错误'}, status=400)
            if not comment_content or len(comment_content) == 0:
                return JsonResponse({'status': 400, 'msg': '评论内容不能为空'}, status=400)
            if len(comment_content) > 500:
                return JsonResponse({'status': 400, 'msg': '评论内容过长'}, status=400)
            if video_id is None:
                return JsonResponse({'status': 400, 'msg': '视频id不能为空'}, status=400)

            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with connection.cursor() as cursor:
                if comment_type == 'comment':
                    sql = '''
                    INSERT INTO comment_table 
                    (send_user_id, comment_content, comment_level, reply_comment_id, send_time, video_id) 
                    VALUES (%s, %s, %s, %s, %s, %s)
                    '''
                    cursor.execute(sql, (user_id, comment_content, 0, comment_id, now, video_id))
                    return JsonResponse({'status': 200, 'msg': '评论成功'}, status=200)

                elif comment_type == 'reply':
                    sql = '''
                    INSERT INTO comment_reply_table 
                    (send_user_id, comment_content, comment_level, reply_comment_id, send_time, belong_to_video_id) 
                    VALUES (%s, %s, %s, %s, %s, %s)
                    '''
                    cursor.execute(sql, (user_id, comment_content, 1, comment_id, now, video_id))
                    return JsonResponse({'status': 200, 'msg': '回复成功'}, status=200)

        except Exception as e:
            logger.error(self.request_path(request) + str(e))
            return JsonResponse({'status': 500, 'msg': '服务器错误'}, status=500)
