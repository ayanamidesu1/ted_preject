import os
import random
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection, transaction
from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from .log.log import Logger
import json
from django.contrib.auth.hashers import check_password, make_password

logger = Logger()

class EditUserInfo(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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
            if not request.user.is_authenticated:
                return JsonResponse({'status': 401, 'msg': '用户未登录'}, status=401)
            user_id = request.user.id
            with connection.cursor() as cursor:

                body_data = request.body.decode('utf-8')
                data = json.loads(body_data) if body_data else {}
                edit_type = data.get('edit_type')

                if edit_type == 'username':
                    return self.edit_username(data, user_id, cursor)
                elif edit_type == 'user_tags':
                    return self.update_field(cursor, user_id, 'user_tags', data.get('user_tags'), '标签不能为空')
                elif edit_type == 'self_website':
                    return self.update_field(cursor, user_id, 'self_website', data.get('self_website'), '网址不能为空')
                elif edit_type == 'self_website_introduce':
                    return self.update_field(cursor, user_id, 'self_website_introduce', data.get('self_website_introduce'), '网址介绍不能为空')
                elif edit_type == 'password':
                    return self.change_password(data, user_id, cursor)
                else:
                    return JsonResponse({'status': 400, 'msg': '未知的修改类型'}, status=400)

        except Exception as e:
            print(e)
            logger.error(e)
            return JsonResponse({'status': 500, 'msg': '服务器错误'}, status=500)

    def edit_username(self, data, user_id, cursor):
        username = data.get('username')
        if not username:
            return JsonResponse({'status': 400, 'msg': '用户名不能为空'}, status=400)

        cursor.execute('SELECT id FROM auth_user WHERE username=%s', [username])
        if cursor.rowcount > 0:
            return JsonResponse({'status': 400, 'msg': '用户名已存在'}, status=400)

        return self.update_field(cursor, user_id, 'username', username)

    def update_field(self, cursor, user_id, field, value, empty_msg=None):
        if not value:
            return JsonResponse({'status': 400, 'msg': empty_msg or '字段不能为空'}, status=400)

        sql = f'UPDATE auth_user SET {field}=%s WHERE id=%s'
        with transaction.atomic():
            cursor.execute(sql, [value, user_id])
            if cursor.rowcount == 1:
                return JsonResponse({'status': 200, 'msg': '修改成功'}, status=200)
            else:
                raise Exception('修改数量异常')

    def change_password(self, data, user_id, cursor):
        once_password = data.get('once_password')
        new_password = data.get('new_password')
        email = data.get('email')

        if not (once_password, new_password, email):
            return JsonResponse({'status': 400, 'msg': '参数错误'}, status=400)

        cursor.execute('SELECT password FROM auth_user WHERE id=%s AND email=%s', [user_id, email])
        if cursor.rowcount != 1:
            return JsonResponse({'status': 400, 'msg': '邮箱错误'}, status=400)

        user_info = cursor.fetchone()
        if not check_password(once_password, user_info[0]):
            return JsonResponse({'status': 400, 'msg': '旧密码错误'}, status=400)

        if len(new_password) < 8 or len(set(new_password)) < 2:
            return JsonResponse({'status': 400, 'msg': '密码不符合要求'}, status=400)

        new_password_hashed = make_password(new_password)
        return self.update_field(cursor, user_id, 'password', new_password_hashed)
