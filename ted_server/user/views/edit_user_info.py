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
from .re_write_img import ReWriteImg
from django.contrib.auth.hashers import make_password

re_write_img = ReWriteImg()
logger = Logger()

class EditUserInfo(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.save_path = os.path.join(os.path.dirname(__file__), '../../static/img/')
        self.thumbnail_path = os.path.join(self.save_path, 'thumbnail')
        self.img_file_path = os.path.join(self.save_path, 'img')

        os.makedirs(self.thumbnail_path, exist_ok=True)
        os.makedirs(self.img_file_path, exist_ok=True)

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
            data = json.loads(request.body.decode('utf-8'))
            edit_type = data.get('edit_type')

            with connection.cursor() as cursor:
                if edit_type == 'username':
                    return self.edit_username(data, user_id, cursor)
                elif edit_type == 'user_tags':
                    return self.update_field(cursor, user_id, 'user_tags',
                                             data.get('user_tags'), '标签不能为空')
                elif edit_type == 'self_website':
                    return self.update_field(cursor, user_id, 'self_website',
                                             data.get('self_website'), '网址不能为空')
                elif edit_type == 'self_website_introduce':
                    return self.update_field(cursor, user_id, 'self_website_introduce',
                                             data.get('self_website_introduce'), '网址介绍不能为空')
                elif edit_type == 'password':
                    return self.change_password(data, user_id, cursor)
                else:
                    return JsonResponse({'status': 400, 'msg': '未知的修改类型'}, status=400)

        except Exception as e:
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

        if not (once_password and new_password and email):
            return JsonResponse({'status': 400, 'msg': '参数错误'}, status=400)

        cursor.execute('SELECT password FROM auth_user WHERE id=%s AND email=%s', [user_id, email])
        if cursor.rowcount != 1:
            return JsonResponse({'status': 400, 'msg': '邮箱错误'}, status=400)

        user_info = cursor.fetchone()
        if user_info[0] != once_password:
            return JsonResponse({'status': 400, 'msg': '密码错误'}, status=400)

        if len(new_password) < 8 or len(set(new_password)) < 2:
            return JsonResponse({'status': 400, 'msg': '密码不符合要求'}, status=400)

        new_password_hashed = make_password(new_password)
        return self.update_field(cursor, user_id, 'password', new_password_hashed)

    def edit_user_avatar(self, request, user_id, cursor):
        file = request.FILES.get('file')
        re_write_img.set_file(file)
        original_img_file = re_write_img.copy_paste()
        thumbnail_file = re_write_img.process_image()

        unique_filename = self.generate_unique_filename(self.img_file_path)
        original_image_path = os.path.join(self.img_file_path, f"{unique_filename}.png")
        thumbnail_image_path = os.path.join(self.thumbnail_path, f"{unique_filename}.png")

        with open(original_image_path, 'wb') as f:
            f.write(original_img_file.read())

        with open(thumbnail_image_path, 'wb') as f:
            f.write(thumbnail_file.read())

        return self.update_field(cursor, user_id, 'avatar_path', unique_filename)

    def generate_unique_filename(self, path):
        while True:
            file_name = ''.join([str(random.randint(0, 9)) for _ in range(21)])
            file_path = os.path.join(path, f"{file_name}.png")
            if not os.path.exists(file_path):
                return file_name
