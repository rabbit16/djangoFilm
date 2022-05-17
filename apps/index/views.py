import json

from django.contrib.auth import login
from django.shortcuts import render,HttpResponse

# Create your views here.
from django.views import View

from index.models import User
from utils.res_code import to_json_data, Code, error_map
from verifications.forms import RegisterForm
from django.contrib.auth import authenticate, login


class index(View):

    def get(self, request):
        return render(request, "index/index.html")

    def post(self, request):
        pass

class Login(View):

    def get(self, request):
        return render(request, "index/login.html")

    # def post(self, request):
    #     return json.dumps({
    #         "errno": '1'
    #     })
    def post(self, request):
        username = request.POST.get['username']
        password = request.POST.get['password']
        # 与数据库中的用户名和密码比对，django默认保存密码是以哈希形式存储，并不是明文密码，这里的password验证默认调用的是User类的check_password方法，以哈希值比较。
        user = authenticate(request, username=username, password=password)
        # 验证如果用户不为空
        if user is not None:
            # login方法登录
            login(request, user)
            # 返回登录成功信息
            return HttpResponse('登陆成功')
        else:
            # 返回登录失败信息
            return HttpResponse('登陆失败')

#
class Register(View):

    def get(self, request):
        return render(request, "index/register.html")

    def post(self, request):
        userInfo = json.loads(request.body.decode())
        if userInfo["gender"] == 'male':
            userInfo["gender"] = True
        else:
            userInfo["gender"] = False
        registerForm = RegisterForm(userInfo)
        try:
            if registerForm.is_valid():
                user = User.objects.create_user(username=registerForm.cleaned_data.get('username'),
                                                password=registerForm.cleaned_data.get('password'),
                                                mobile=registerForm.cleaned_data.get('mobile'),
                                                email=registerForm.cleaned_data.get('email'),
                                                sex=registerForm.cleaned_data.get("gender"),
                                                name=registerForm.cleaned_data.get("real_name"),
                                                birthday=registerForm.cleaned_data.get("birthday")
                                                )  # TODO 并没有写完整
                login(request, user)
            data = {
                'errno': Code.OK
            }
            return to_json_data(data=data)
        except:
            return to_json_data(errno=Code.NODATA, errmsg=error_map[Code.PICERROR])