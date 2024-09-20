from django.shortcuts import render,redirect
from .forms import User_creation,edit_user_form
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from .models import Profile
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
            messages.success(request,'User created, Welcome')
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
            first_name=user.first_name
        except:
            messages.error(request,'invalid username or password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,f'Welcome {first_name}',)
            return redirect('home')
        else:
            messages.error(request,'invalid password')
    return render(request,'users/login.html')

#user logout
@login_required(login_url='login_user')
def user_logout(request):
    logout(request)
    messages.success(request,'Logout successful')
    return redirect('login_user')

#user info rendering and editing
@login_required(login_url='login_user')
def user_profile(request):
    profile=request.user.profile
    form =edit_user_form(instance=profile)

    if request.method=='POST':
        form=edit_user_form(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save(commit=False)
            
            messages.success(request,'Profile Updated')
            return redirect('home')
    context={
        'user_info':profile,
        'form':form,
    }

    return render(request,'users/user_profile.html',context)