from django.db import connection
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from datetime import datetime
from ..log.log import Logger
import json
import random

logger = Logger()


class RecommendVideo(APIView):
    def request_path(self, request):
        request_ip = request.META.get('REMOTE_ADDR', '未知IP')
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f'{request_ip} 在 {now} 访问了 {request.path}'

    def get(self, request):
        logger.warning(self.request_path(request) + str(request.user))
        return render(request, '404.html', status=404)

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode('utf-8'))
            with connection.cursor() as cursor:
                sql = '''select * ,video_info.id as 'video_id'  
                from video_info left join auth_user on auth_user.id=video_info.author_id'''
                cursor.execute(sql)
                result = cursor.fetchall()
                columns = [column[0] for column in cursor.description]
                rows = [dict(zip(columns, row)) for row in result]

                # 使用 id 去重
                unique_rows = {row['id']: row for row in rows}.values()

                # 如果去重后视频不足 15 个，补满并允许重复选择
                if len(unique_rows) < 15:
                    # 允许重复，扩展列表
                    extended_rows = list(unique_rows) * (15 // len(unique_rows) + 1)
                    random_arr = random.sample(extended_rows, 15)
                else:
                    # 如果视频数量充足，从去重后的视频中随机选择15个
                    random_arr = random.sample(list(unique_rows), 15)
                sql='''
                select count(*) as 'watch_count' from watch_table where video_id=%s
                '''

                for row in random_arr:
                    cursor.execute(sql,[row.get('video_id')])
                    row['watch_count']=cursor.fetchone()[0]
                    row.pop('id', None)
                    row.pop('password',None)
                    row.pop('email',None)


                # 返回 JSON 响应
                return JsonResponse({'status': 200, 'data': random_arr},status=200)

        except Exception as e:
            logger.error(e)
            return Response({'status': 500, 'msg': '服务器错误'}, status=500)
