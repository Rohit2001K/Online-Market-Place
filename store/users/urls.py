from django.urls import path
from . import views

#Urls

urlpatterns=[
    path('',views.add_user,name='add_user'),
    path('login/',views.user_login,name='login_user'),
    path('logout/',views.user_logout,name='logout_user'),
    path('user-info/',views.user_profile,name='user_profile'),
    path('seller-info/<str:pk>',views.seller_profile,name='seller_profile'),
    path('user-inbox/',views.inbox,name='inbox'),
    path('message/<str:pk>',views.message_box,name='message'),
    path('send-message/<str:pk>', views.send_message, name='send_message'),
    path('reply/<str:pk>', views.reply_message, name='reply_message'),
    path('delete-message/<str:pk>', views.message_del, name='delete_message'),
]