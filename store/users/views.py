from django.shortcuts import render,redirect
from .forms import User_creation
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from .models import Profile
from django.http import HttpResponse
# Create your views here.

#user creation
def add_user(request):
    form=User_creation()
    if request.method=='POST':
        form=User_creation(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
    return render(request,'users/signup.html',{'form':form})



#User Login

def user_login(request):
    if request.user.is_authenticated:
       return redirect('home') 
    if request.method=='POST':
        username=request.POST['username']
        username=username.lower()
        password=request.POST['password']
        try:
            user=User.objects.get(username=username)
        except:
            return HttpResponse("NO USERNAME FOUND")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("INVALID PASSWORD")
    return render(request,'users/login.html')

#user logout
def user_logout(request):
    logout(request)
    return redirect('login_user')

#user info rendering

def user_profile(request):
    user_info=request.user.profile
    context={
        'user_info':user_info,
    }

    return render(request,'users/user_profile.html',context)