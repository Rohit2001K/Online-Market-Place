from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Product,Tag
from .forms import product_upload_from
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.



#market home page
def market_page(request):
    #seach
    search=''
    if request.GET.get('search'):
        search=request.GET.get('search')
    tag=Tag.objects.filter(tag_type__icontains=search)  
    products= Product.objects.distinct().filter(
        Q(title__icontains=search) |
        Q(tags__in=tag)
        )
    
    #For pagination
    page=request.GET.get('page')
    result=6
    pag=Paginator(products,result)
    try:
        products=pag.page(page)
    except PageNotAnInteger:
        products=pag.page(1)
    except EmptyPage:
        page=pag.num_pages
        products=pag.page(page)
    #Pagination end

    content={
        'products':products,
        'search':search,
        'pag':pag
    }
    return render(request,'market/market_page.html',content)



#product detail page 
@login_required(login_url='login_user')
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
            form.save_m2m() 
            messages.success(request,'Product is Uploaded')
            return redirect('home')
        else:
            print(form.errors)
            messages.error(request,'Please Fill all fields properly')
    content={
        'form':form,
    }
    return render(request,'market/upload_product.html',content)