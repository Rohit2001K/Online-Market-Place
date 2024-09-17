from django.db import models
from django.contrib.auth.models import User
import uuid
#import for signals 
from django.db.models.signals import post_save


# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    username=models.CharField(max_length=20,null=False,unique=True)
    first_name=models.CharField(max_length=20,null=False)
    last_name=models.CharField(max_length=50,null=False)
    email=models.EmailField()
    id=models.UUIDField(default=uuid.uuid1,primary_key=True)
    pic=models.ImageField(default='user/user.jpg',upload_to='user/')
    
    def __str__(self):
        return str(self.username)
    



#signals for user creation
def profile_creation(sender,instance,created,**kwargs):
    if created:
        user=instance
        profile=Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email
        )

post_save.connect(profile_creation,sender=User)


#signals for user edit

def edit_profile(sender,instance,created,**kwargs):
    profile=instance
    user=profile.user
    if created==False:
        user.first_name=profile.name
        user.email=profile.email
        user.save()

post_save.connect(edit_profile,sender=Profile)