from django.shortcuts import render
from .models import Product
# Create your views here.



#market home page

def market_page(request):
    products=Product.objects.all()
    content={
        'products':products
    }
    return render(request,'market/market_page.html',content)
