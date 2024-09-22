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
            messages.error(request,'Please Fill all fields properly')
    content={
        'form':form,
    }
    return render(request,'market/upload_product.html',content)



#Show owner his uploaded products
@login_required(login_url='login_user')
def user_product_page(request):
    owner=request.user.profile
    user_products=Product.objects.filter(owner=owner)
    content={
        'user_products':user_products,
    }
    return render(request,'market/user_product_page.html',content)




#Using same form for editing products
@login_required(login_url='login_user')
def edit_product(request,pk):
    owner=request.user.profile
    product=Product.objects.get(product_id=pk)
    if owner == product.owner:                                                 #Making sure that only requested user is owner of that product
        if request.method == 'POST':
            form = product_upload_from(request.POST, request.FILES, instance=product)
            if form.is_valid():
                form.save()
                messages.success(request, 'Product Edited')
                return redirect('home')
            else:
                messages.error(request, 'Please fill all fields properly')
        else:
            form = product_upload_from(instance=product) 
    else:
        messages.error(request, 'You are not authorized to edit this product')
        return redirect('home')

    content = {
        'form': form,
    }
    return render(request, 'market/upload_product.html', content)


#Product deletion
@login_required(login_url='login_user')
def product_delete(request,pk):
    owner=request.user.profile 
    product=Product.objects.get(product_id=pk)
    if owner==product.owner:                                                     #Making sure that only requested user is owner of that product
        product.delete()
        messages.success(request, 'Product Deleted')
        return redirect('home')
    else:
        messages.error(request, 'You are not authorized to delete this product')
        return redirect('home')
