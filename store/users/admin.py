from django.contrib import admin
from .models import Profile,inbox_messages
# Register your models here.


admin.site.register(Profile)
admin.site.register(inbox_messages)