from django.urls import path
from . import views

#Urls

urlpatterns=[
    path('',views.add_user,name='add_user'),
    path('login/',views.user_login,name='login_user'),
    path('logout/',views.user_logout,name='logout_user'),
    path('user-info/',views.user_profile,name='user_profile'),
    path('user-inbox/',views.inbox,name='inbox'),
]