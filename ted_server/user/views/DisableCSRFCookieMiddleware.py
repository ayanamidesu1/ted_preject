# 创建一个新的中间件类
class DisableCSRFCookieMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 处理请求
        response = self.get_response(request)
        return response

    def process_response(self, request, response):
        # 禁止设置 CSRF cookie
        if 'Set-Cookie' in response:
            response['Set-Cookie'] = response['Set-Cookie'].replace('csrf', 'disabled_csrf')  # 随意替换，防止 CSRF cookie 的设置
        return response
