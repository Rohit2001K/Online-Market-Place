from django.shortcuts import render

# Create your views here.


#market home page

def market_page(request):
    return render(request,'market/market_page.html')
