from django.urls import path
from . import views



#market urls

urlpatterns=[
    path('',views.market_page,name='market')
]