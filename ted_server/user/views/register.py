import hashlib
import os
import json
import random
from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render
from django.db import connection, transaction
from django.views import View
from .log.log import Logger
from .re_write_img import ReWriteImg
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt


class RegisterView(View):
    logger = Logger()
    rewrite_img = ReWriteImg(200, 200)
    permission_classes = [AllowAny]

    @csrf_exempt
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_img_root_path = 'H:/ted_preject/ted_server/static/img/'
        self.save_path = os.path.join(os.path.dirname(__file__), '../../static/img/')
        self.thumbnail_path = os.path.join(self.save_path, 'thumbnail')
        self.img_file_path = os.path.join(self.save_path, 'img')

        # 确保目录存在
        os.makedirs(self.thumbnail_path, exist_ok=True)
        os.makedirs(self.img_file_path, exist_ok=True)

    # 生成21位随机数字文件名
    def generate_unique_filename(self, path):
        while True:
            file_name = ''.join([str(random.randint(0, 9)) for _ in range(21)])
            file_path = os.path.join(path, file_name + ".jpg")
            if not os.path.exists(file_path):
                return file_name

    def request_path(self, request):
        request_path = request.path
        request_ip = request.META['REMOTE_ADDR']
        now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        request_content = request.body.decode('utf-8')
        return f'{request_ip}在{now}访问了{request_path}'

    def get(self, request):
        self.logger.warning(self.request_path(request))
        return render(request, '404.html')

    def post(self, request, *args, **kwargs):
        try:
            # 从 request.POST 中获取用户信息
            userinfo_json = request.POST.get('userinfo')
            if not userinfo_json:
                return JsonResponse({'status': '400', 'msg': '用户信息缺失'}, status=400)

            userinfo = json.loads(userinfo_json)

            # 从 request.FILES 中获取文件
            file = request.FILES.get('file')
            if not file:
                self.logger.warning(self.request_path(request) + '，没有文件上传')
                return JsonResponse({'status': '400', 'msg': '没有文件上传'}, status=400)

            # 生成唯一文件名
            unique_filename = self.generate_unique_filename(self.img_file_path)

            # 处理图像
            self.rewrite_img.set_file(file)
            original_img_file = self.rewrite_img.copy_paste()
            thumbnail_file = self.rewrite_img.process_image()

            # 保存缩略图和原始图像
            original_image_path = os.path.join(self.img_file_path, f"{unique_filename}.png")
            thumbnail_image_path = os.path.join(self.thumbnail_path, f"{unique_filename}.png")

            # 将原始图像保存
            with open(original_image_path, 'wb') as f:
                f.write(original_img_file.read())

            # 将缩略图保存到指定路径
            with open(thumbnail_image_path, 'wb') as f:
                f.write(thumbnail_file.read())

            # 更新文件路径
            avatar_path = f"/static/img/img/{unique_filename}.jpg"

            with transaction.atomic():
                with connection.cursor() as cursor:
                    sql = ''' 
                    INSERT INTO auth_user (password, last_login, is_superuser, username, first_name, last_name, email,
                    is_staff, is_active, date_joined, avatar_path, sex, birthday) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    '''
                    # 密码加密
                    password = make_password(userinfo.get('password', None))
                    last_login = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    is_superuser = 0
                    username = userinfo.get('username', None)
                    first_name = userinfo.get('first_name', None)
                    last_name = userinfo.get('last_name', None)
                    email = userinfo.get('email', None)
                    is_staff = 1
                    is_active = 1
                    date_joined = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    sex = userinfo.get('sex', None)
                    birthday = userinfo.get('birthday', None)
                    cursor.execute(sql, [password, last_login, is_superuser, username, first_name, last_name,
                                         email, is_staff, is_active, date_joined, unique_filename, sex, birthday])

            return JsonResponse({'status': '201', "msg": "注册成功"}, status=201)

        except Exception as e:
            self.logger.error(self.request_path(request) + f'，错误信息为{e}')
            return JsonResponse({'status': '500', 'msg': '服务器错误，请稍后重试'}, status=500)
