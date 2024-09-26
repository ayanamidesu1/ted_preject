from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.db import transaction,connection
from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from .log.log import Logger

logger = Logger()


class GetUserInfo(APIView):
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
            # 如果用户已登录
            if request.user.is_authenticated:
                user = request.user
                userinfo = {
                    "username": user.username,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "is_staff": user.is_staff,
                    "is_superuser": user.is_superuser,
                    "is_active": user.is_active,
                    "last_login": user.last_login,
                    "date_joined": user.date_joined,
                    "id": user.id,
                }
                user_data = {}
                sql='''
                    select * from auth_user where id=%s
                '''
                with connection.cursor() as cursor:
                    cursor.execute(sql, [user.id])
                    user_data = dict(zip([col[0] for col in cursor.description], cursor.fetchone()))

                if user_data:
                    user_data.pop('password', None)  # 移除密码字段
                    return JsonResponse({'status': 200, 'data': user_data}, status=200)

            else:
                return JsonResponse({'status': 403, 'message': '用户未登录'}, status=403)

        except Exception as e:
            logger.error(str(e))
            return JsonResponse({'status': 500, 'message': '服务器内部错误'}, status=500)
