from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect
from teacher.models import Teacher


# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User(first_name=request.POST['fname'], username=request.POST['email'], email=request.POST['email'])
                user.set_password(request.POST['password1'])
                user.is_active = False
                user.save()
                return render(request, 'signup.html',
                              {'msg': 'Please Stand by. We will send you an email when your teacher has verified you..'})
            except IntegrityError:
                return render(request, 'signup.html',
                              {'msg': 'Account with this email already exists'})



        else:
            return render(request, 'signupuser.html',
                          {'form': UserCreationForm(), 'msg': 'Passwords did not match'})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['email'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html',
                          {'form': AuthenticationForm(), 'msg': 'Username or Password Incorrect'})
        else:
            login(request, user)
            if Teacher.objects.filter(user=user).exists():
                return redirect('/teacher')
            return redirect('/student')


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
