from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,inbox_messages
from django.forms import ImageField,FileInput


#custom user creation forms
class User_creation(UserCreationForm):
    class Meta:
        model=User
        fields=[
            'email',
            'username',
            'password1',
            'password2'
        ]

        lables={
            'password1':'Password',
            'password2':'Enter Password Again'
        }


#placeholder for user_create form

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Username',
            'class': 'form-input'
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Email',
            'class': 'form-input'
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Password',
            'class': 'form-input'
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Confirm Password',
            'class': 'form-input'
        })



#user edit profile form
class edit_user_form(ModelForm):
    pic=ImageField(widget=FileInput)
    class Meta:
        model=Profile
        fields=[
            'first_name',
            'last_name',
            'email',
            'pic'
        ]




#message form

class SendMessage(ModelForm):
    class Meta:
        model=inbox_messages
        fields=[
            'body'
        ]