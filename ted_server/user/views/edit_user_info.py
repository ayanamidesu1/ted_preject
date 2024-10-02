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
from django.conf import settings  # 使用Django settings获取路径

re_write_img = ReWriteImg()
logger = Logger()


class EditUserInfo(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 使用settings获取路径，避免硬编码
        self.save_path = os.path.join(settings.BASE_DIR, 'static/img/')
        self.thumbnail_path = os.path.join(self.save_path, 'thumbnail')
        self.img_file_path = os.path.join(self.save_path, 'img')

        # 确保目录存在
        os.makedirs(self.thumbnail_path, exist_ok=True)
        os.makedirs(self.img_file_path, exist_ok=True)

    def request_path(self, request):
        request_ip = request.META.get('REMOTE_ADDR', '未知IP')
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f'{request_ip} 在 {now} 访问了 {request.path}'

    def get(self, request):
        logger.warning(self.request_path(request) + str(request.user))
        return render(request, '404.html', status=404)

    def post(self, request):
        try:
            # 用户未登录
            if not request.user.is_authenticated:
                return JsonResponse({'status': 401, 'msg': '用户未登录'}, status=401)

            user_id = request.user.id
            data = json.loads(request.body.decode('utf-8'))

            # 根据edit_type调用相应的方法
            edit_type = data.get('edit_type')
            with connection.cursor() as cursor:
                if edit_type == 'avatar':
                    return self.edit_user_avatar(request, user_id, cursor)
                else:
                    return self.edit_foundation_info(request, user_id, cursor, edit_type)

        except Exception as e:
            logger.error(e)
            return JsonResponse({'status': 500, 'msg': '服务器错误'}, status=500)

    def edit_user_avatar(self, request, user_id, cursor):
        try:
            file = request.FILES.get('file')
            re_write_img.set_file(file)
            original_img_file = re_write_img.copy_paste()
            thumbnail_file = re_write_img.process_image()

            # 生成唯一文件名
            unique_filename = self.generate_unique_filename(self.img_file_path)

            # 保存缩略图和原始图像
            original_image_path = os.path.join(self.img_file_path, f"{unique_filename}.png")
            thumbnail_image_path = os.path.join(self.thumbnail_path, f"{unique_filename}.png")

            # 将原始图像保存
            with open(original_image_path, 'wb') as f:
                f.write(original_img_file.read())

            # 将缩略图保存到指定路径
            with open(thumbnail_image_path, 'wb') as f:
                f.write(thumbnail_file.read())

            sql = 'UPDATE auth_user SET avatar_path=%s WHERE id=%s'
            with transaction.atomic():
                cursor.execute(sql, (unique_filename, user_id))
                if cursor.rowcount == 1:
                    return JsonResponse({'status': 200, 'msg': '修改成功'}, status=200)
                else:
                    raise Exception('修改数量异常')

        except Exception as e:
            logger.error(e)
            return JsonResponse({'status': 500, 'msg': '服务器错误'}, status=500)

    def edit_foundation_info(self, request, user_id, cursor, edit_type):
        data = json.loads(request.body.decode('utf-8'))
        fields_mapping = {
            'username': '用户名',
            'user_tags': '标签',
            'self_website': '网址',
            'self_website_introduce': '网址介绍'
        }

        if edit_type in fields_mapping:
            field_value = data.get(edit_type, False)
            if field_value:
                return self.update_field(cursor, edit_type, field_value, user_id, fields_mapping[edit_type])
            else:
                return JsonResponse({'status': 400, 'msg': f'{fields_mapping[edit_type]}不能为空'}, status=400)

        elif edit_type == 'password':
            return self.edit_password(request, user_id, cursor)
        else:
            return JsonResponse({'status': 400, 'msg': '无效的修改类型'}, status=400)

    def update_field(self, cursor, field, value, user_id, field_name):
        sql = f'UPDATE auth_user SET {field}=%s WHERE id=%s'
        try:
            with transaction.atomic():
                cursor.execute(sql, [value, user_id])
                if cursor.rowcount == 1:
                    return JsonResponse({'status': 200, 'msg': '修改成功'}, status=200)
                else:
                    raise Exception('修改数量异常')
        except Exception as e:
            logger.error(e)
            return JsonResponse({'status': 500, 'msg': f'{field_name}修改失败'}, status=500)

    def edit_password(self, request, user_id, cursor):
        data = json.loads(request.body.decode('utf-8'))
        once_password = data.get('once_password', False)
        new_password = data.get('new_password', False)
        email = data.get('email', False)
        username = request.user.username

        if once_password and new_password and email:
            cursor.execute('SELECT password FROM auth_user WHERE username=%s AND email=%s', [username, email])
            if cursor.rowcount == 1:
                current_password = cursor.fetchone()[0]
                if current_password == once_password:
                    if len(new_password) < 8:
                        return JsonResponse({'status': 400, 'msg': '密码长度不能小于8位'}, status=400)
                    if len(set(new_password)) < 2:
                        return JsonResponse({'status': 400, 'msg': '密码必须包含两种不同的字符'}, status=400)

                    new_password_hashed = make_password(new_password)
                    sql = 'UPDATE auth_user SET password=%s WHERE id=%s'
                    with transaction.atomic():
                        cursor.execute(sql, [new_password_hashed, user_id])
                        if cursor.rowcount == 1:
                            return JsonResponse({'status': 200, 'msg': '修改成功'}, status=200)
                        else:
                            raise Exception('修改数量异常')
                else:
                    return JsonResponse({'status': 400, 'msg': '原密码错误'}, status=400)
            else:
                return JsonResponse({'status': 400, 'msg': '邮箱错误'}, status=400)
        else:
            return JsonResponse({'status': 400, 'msg': '参数错误'}, status=400)

    def generate_unique_filename(self, path):
        while True:
            file_name = ''.join([str(random.randint(0, 9)) for _ in range(21)])
            file_path = os.path.join(path, file_name + ".png")
            if not os.path.exists(file_path):
                return file_name
