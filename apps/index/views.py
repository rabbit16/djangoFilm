import json
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class index(View):

    def get(self, request):
        return render(request, "index/index.html")

    def post(self, request):
        pass

class Login(View):

    def get(self, request):
        return render(request, "index/login.html")

    def post(self, request):
        return json.dumps({
            "errno": '1'
        })
#
class Register(View):
#
    def get(self, request):
        return render(request, "index/register.html")
#
    def post(self, request):
        data = json.loads(request.body)
        print(data["username"])
        return JsonResponse({
            "hello": 2
        })