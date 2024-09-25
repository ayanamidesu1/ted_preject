from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse, Http404
import jwt
from django.conf import settings
import random
import string


class CustomCSRFMiddleware(MiddlewareMixin):
    secret_key = 'django-insecure-e_$uf9(uekzu)d6xr6g1lsb+im88_py@9=3n&3-hp#a(&)^g0^'

    def process_request(self, request):
        # 处理 GET 请求以分发 CSRF Token
        if request.method == 'GET':
            # 生成 CSRF Token
            csrf_token = self.generate_csrf_token()
            return JsonResponse({'csrfToken': csrf_token})

        # 处理 POST 请求以验证 CSRF Token
        if request.method == 'POST':
            csrf_token = request.META.get('csrf_token')
            if not csrf_token or not self.validate_csrf_token(csrf_token):
                return JsonResponse({'error': 'Invalid CSRF Token'}, status=403)

        return None

    def generate_csrf_token(self):
        #使用秘钥生成随机字符串
        token = jwt.encode({'nonce': ''.join(random.choices(string.ascii_letters + string.digits, k=32))},
                           self.secret_key, algorithm='HS256')
        return token  # 这里返回生成的 CSRF Token

    def validate_csrf_token(self, token):
        #通过秘钥验证token
        try:
            jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return True
        except jwt.InvalidTokenError:
            return False
