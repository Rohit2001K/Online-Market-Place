from django.shortcuts import render,redirect
from .forms import User_creation,edit_user_form,SendMessage
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from .models import Profile,inbox_messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from market.models import Product
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
            form.save()
            messages.success(request,'Profile Updated')
            return redirect('home')
    context={
        'user_info':profile,
        'form':form,
    }

    return render(request,'users/user_profile.html',context)


#Showing Seller Profile
@login_required(login_url='login_user')
def seller_profile(request,pk):
    product=Product.objects.get(product_id=pk)
    seller=product.owner
    content={
        'seller':seller
    }
    return render(request,'users/seller_profile.html',content)




#messages for inbox
@login_required(login_url='login_user')
def inbox(request):
    user=request.user.profile
    msg=user.inbox_msg.all()
    unread_messages=msg.filter(is_read=False).count()
    content={
        'msg':msg,
        'unread_messages':unread_messages
    }
    return render(request,'users/inbox.html',content)


#message opening
@login_required(login_url='login_user')
def message_box(request,pk):
    user=request.user.profile
    msg=user.inbox_msg.get(id=pk)
    msg.is_read=True
    msg.save()
    content={
        'msg':msg

    }
    return render(request,'users/message.html',content)


#sending mesages
@login_required(login_url='login_user')
def send_message(request,pk):
    reciver_product=Product.objects.get(product_id=pk)
    sender_user=request.user.profile  
    form=SendMessage() 
    if request.method=='POST':
        form=SendMessage(request.POST)
        if form.is_valid():
            form_save=form.save(commit=False)
            form_save.sender=sender_user
            form_save.reciver=reciver_product.owner
            form_save.product=reciver_product
            form_save.email=sender_user.email
            form_save.save()
            messages.success(request,'Message Send!')
            return redirect('home')
    content={
        'form':form

    }
    return render(request,'users/message_sending_form.html',content)


#Message reply
@login_required(login_url='login_user')
def reply_message(request,pk):
    message_id=inbox_messages.objects.get(id=pk)
    form=SendMessage() 
    if request.method=='POST':
        form=SendMessage(request.POST)
        if form.is_valid():
            form_save=form.save(commit=False)
            form_save.sender=request.user.profile
            form_save.reciver=message_id.sender
            form_save.product=message_id.product
            form_save.email=request.user.profile.email
            form_save.save()
            messages.success(request,'Message Send!')
            return redirect('home')
    content={
        'form':form

    }
    return render(request,'users/message_sending_form.html',content)


#message delete
@login_required(login_url='login_user')
def message_del(request,pk):
    message=inbox_messages.objects.get(id=pk)
    message.delete()
    return redirect('inbox')