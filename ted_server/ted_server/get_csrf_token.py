from django.http import JsonResponse
from django.views import View
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt

class CSRFTokenView(View):
    @csrf_exempt  # 不需要进行 CSRF 检查
    def get(self, request):
        # 打印请求信息以便调试
        print("Request received:", request)
        # 获取 CSRF Token
        csrf_token = get_token(request)

        if csrf_token:
            print("CSRF Token generated:", csrf_token)
        else:
            print("Failed to generate CSRF Token")

        # 以 JSON 格式返回 CSRF Token
        return JsonResponse({'csrfToken': csrf_token})
