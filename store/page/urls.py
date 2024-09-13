from django.urls import path
from . import views

#Home page urls

urlpatterns=[
    path('',views.home_page)
]