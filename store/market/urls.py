from django.urls import path
from . import views



#market urls

urlpatterns=[
    path('',views.market_page,name='market'),
    path('product/<str:pk>/',views.detail_product,name='detail_product'),
    path('upload-product/',views.upload_product,name='upload_product'),
]