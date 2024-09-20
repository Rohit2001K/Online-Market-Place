from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Product
from .forms import product_upload_from
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.



#market home page
def market_page(request):
    products=Product.objects.all()
    content={
        'products':products
    }
    return render(request,'market/market_page.html',content)



#detail page 
def detail_product(request,pk):
    iteam=Product.objects.get(product_id=pk)
    content={
        'iteam':iteam,
    }
    
    return render(request,'market/detail_product.html',content)


#product upload page
@login_required(login_url='login_user')
def upload_product(request):
    owner=request.user.profile
    form=product_upload_from()
    if request.method=='POST':
        form=product_upload_from(request.POST,request.FILES)
        if form.is_valid():
            owner_id=form.save(commit=False)
            owner_id.owner=owner
            owner_id.save()
            messages.success(request,'Product is Uploaded')
            return redirect('home')
        else:
            messages.error(request,'Please Fill all fields properly')
    content={
        'form':form,
    }
    return render(request,'market/upload_product.html',content)