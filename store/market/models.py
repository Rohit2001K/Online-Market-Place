from django.db import models
import uuid

# Create your models here.

class Tag(models.Model):
    types=(
        
        ('mobiles', 'Mobiles'),
        ('smartphones', 'Smartphones'),
        ('laptops', 'Laptops'),
        ('electronics', 'Electronics'),
        ('computers', 'Computesr'),
        ('fashion_and_clothes', 'Fashion and Clothes'),
        ('houses', 'Houses'),
        ('rentes', 'Rentes'),
        ('cars', 'Cars'),
        ('bikes', 'Bikes'),

    )
    tag_type=models.CharField(max_length=20,choices=types,default=None,null=True,blank=True)

    def __str__(self):
        return str(self.tag_type)


class Product(models.Model):
    owner=models.ForeignKey('users.Profile',on_delete=models.CASCADE)
    product_id=models.UUIDField(default=uuid.uuid1,primary_key=True)
    title=models.CharField(max_length=50,null=False)
    short_discription=models.CharField(max_length=100,null=True,blank=True,default='')
    discription=models.TextField(max_length=500,null=True,blank=True)
    price=models.IntegerField(default=0,null=False)
    main_img=models.ImageField(default='default/market.png',upload_to='iteams/')
    sub_img1=models.ImageField(default='default/market.png',upload_to='iteams/')
    sub_img2=models.ImageField(default='default/market.png',upload_to='iteams/')
    sub_img3=models.ImageField(default='default/market.png',upload_to='iteams/')
    sub_img4=models.ImageField(default='default/market.png',upload_to='iteams/')
    ownership_type_options=(
        ('1st','1st Owner'),
        ('2nd','2nd Owner'),
        ('2nd+','More than 2nd'),
    )
    ownership_type=models.CharField(max_length=50,choices=ownership_type_options,default=None)
    purchase_date=models.DateField(null=True,blank=True)
    bill_and_box_options=(
        ('Yes','Have either bill/box'),
        ('No',"I don't have bill or box")
    )
    bill_and_box=models.CharField(choices=bill_and_box_options,max_length=50,default=None,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    tags=models.ManyToManyField(Tag,blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering=['-created']
    