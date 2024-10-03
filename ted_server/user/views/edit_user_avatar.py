import os
import random
from django.http import JsonResponse
from django.db import transaction
from .re_write_img import ReWriteImg
from rest_framework.views import APIView
from datetime import datetime
from .log.log import Logger
from django.shortcuts import render
from django.db import connection

logger=Logger

class EditUserAvatar(APIView):
    def __init__(self):
        self.re_write_img = ReWriteImg()
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

    def post(self, request,*args,**kwargs):
        user_id = request.user.id
        if request.user.is_authenticated:
            with connection.cursor() as cursor:
                try:
                    return self.edit_avatar(request, user_id, cursor)
                except Exception as e:
                    logger.error(f'修改头像失败，错误信息为：{str(e)}')
                    return JsonResponse({'status': 500, 'msg': '修改头像失败'}, status=500)


    def edit_avatar(self, request, user_id, cursor):
        file = request.FILES.get('file')
        self.re_write_img.set_file(file)
        original_img_file = self.re_write_img.copy_paste()
        thumbnail_file = self.re_write_img.process_image()

        unique_filename = self.generate_unique_filename(self.img_file_path)
        original_image_path = os.path.join(self.img_file_path, f"{unique_filename}.png")
        thumbnail_image_path = os.path.join(self.thumbnail_path, f"{unique_filename}.png")

        with open(original_image_path, 'wb') as f:
            f.write(original_img_file.read())

        with open(thumbnail_image_path, 'wb') as f:
            f.write(thumbnail_file.read())

        return self.update_avatar_path(cursor, user_id, unique_filename)

    def update_avatar_path(self, cursor, user_id, filename):
        sql = 'UPDATE auth_user SET avatar_path=%s WHERE id=%s'
        with transaction.atomic():
            cursor.execute(sql, [filename, user_id])
            if cursor.rowcount == 1:
                return JsonResponse({'status': 200, 'msg': '头像修改成功'}, status=200)
            else:
                raise Exception('修改数量异常')

    def generate_unique_filename(self, path):
        while True:
            file_name = ''.join([str(random.randint(0, 9)) for _ in range(21)])
            file_path = os.path.join(path, f"{file_name}.png")
            if not os.path.exists(file_path):
                return file_name
