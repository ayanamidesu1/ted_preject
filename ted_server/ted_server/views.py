from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    # 重写认证逻辑，支持用户名或邮箱认证
    username_field = 'username'

    def validate(self, attrs):
        username_or_email = attrs.get("username")  # 这里可以是用户名或邮箱
        password = attrs.get("password")

        # 尝试通过用户名认证
        user = authenticate(username=username_or_email, password=password)

        # 如果用户名认证失败，尝试通过邮箱认证
        if user is None:
            try:
                # 查找用户对象
                user_obj = User.objects.get(email=username_or_email)
                # 使用用户名进行认证，而不是邮箱
                user = authenticate(username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None

        # 验证用户是否存在并且密码正确
        if user:
            # 调用父类的 `validate` 方法生成 Token
            data = super().validate(attrs)
            data['status'] = 200  # 自定义返回状态码
            return data
        else:
            raise serializers.ValidationError('用户名/邮箱或密码不正确')


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
