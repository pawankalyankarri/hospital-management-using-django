from django.shortcuts import render,redirect
from django.views import View
# Create your views here.

class Login(View):
    def get(self,req):
        return render(req,'login/login.html')
    def post(self,req):
        print(req.POST)
        return redirect('loginurl')