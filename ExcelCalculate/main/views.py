from django.shortcuts import render, redirect
from .models import *
from random import randint

# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def signup(request):
    return render(request, 'main/signup.html')


def signin(request):
    return render(request, 'main/signin.html')


def verifyCode(request):
    return render(request, 'main/verifyCode.html')

def verify(request):
    return redirect('main_index')


def result(request):
    return render(request, 'main/result.html')


def join(request):
    name = request.POST['signupName']
    email = request.POST['signupEmail']
    pw = request.POST['signupPW']
    user = User(user_name= name, user_email=email, user_password = pw)
    user.save()
    code = randint(1000, 9999)
    response = redirect('main_veriifyCode')
    response.set_cookie('code', code)
    response.set_cookie('user_id', user.id)
    return response