from django.forms import ModelForm
from .models import Product
from django.forms import ImageField,FileInput
from django import forms
#Custom product upload form

class product_upload_from(ModelForm):
    #main_img=ImageField(widget=FileInput)
    class Meta:
        model=Product
        fields=[
            'title',
            'short_discription',
            'discription',
            'price',
            'ownership_type',
            'bill_and_box',
            'purchase_date',
            'main_img',
            'sub_img1',
            'sub_img2',
            'sub_img3',
            'sub_img4',
            'tags',
        ]

        widgets = {
            'discription': forms.Textarea(attrs={'class': 'textarea'}),
            'purchase_date': forms.DateInput(attrs={'class': 'date-picker', 'type': 'date'}),
            'title': forms.TextInput(attrs={'class': 'input-field'}),
            'short_discription': forms.TextInput(attrs={'class': 'input-field'}),
            'ownership_type': forms.Select(attrs={'class': 'input-field'}),
            'price': forms.NumberInput(attrs={'class': 'input-field'}),
            'bill_and_box': forms.Select(attrs={'class': 'input-field'}),
            'main_img': forms.ClearableFileInput(attrs={'class': 'input-field'}),
            'sub_img1': forms.ClearableFileInput(attrs={'class': 'input-field'}),
            'sub_img2': forms.ClearableFileInput(attrs={'class': 'input-field'}),
            'sub_img3': forms.ClearableFileInput(attrs={'class': 'input-field'}),
            'sub_img4': forms.ClearableFileInput(attrs={'class': 'input-field'}),
            'tags': forms.SelectMultiple(attrs={'class': 'input-field'}), 
        }

        