from django.urls import path
from . import views



#market urls

urlpatterns=[
    path('',views.market_page,name='market'),
    path('product/<str:pk>/',views.detail_product,name='detail_product'),
    path('upload-product/',views.upload_product,name='upload_product'),
    path('edit-product/<str:pk>',views.edit_product,name='edit_product'),
    path('delete-product/<str:pk>',views.product_delete,name='delete_product'),
    path('my-product/',views.user_product_page,name='my_product'),
]