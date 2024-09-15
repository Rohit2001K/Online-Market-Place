from django.urls import path
from . import views

#Urls

urlpatterns=[
    path('',views.add_user,name='add_user'),
    path('login/',views.user_login,name='login_user'),
    path('logout/',views.user_logout,name='logout_user')
]