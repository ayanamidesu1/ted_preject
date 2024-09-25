# user/middleware.py
from django.utils.deprecation import MiddlewareMixin

class DisableCSRFCookieMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        # 禁止设置 CSRF cookie
        if 'Set-Cookie' in response:
            response['Set-Cookie'] = response['Set-Cookie'].replace('csrf', 'disabled_csrf')  # 随意替换，防止 CSRF cookie 的设置
        return response
