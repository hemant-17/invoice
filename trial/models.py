from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save


# Create your models here.



class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=150)
    #outstanding = models.IntegerField()
    def __str__(self):
        return self.customer_name

class Invoice(models.Model):
    invoice_id = models.IntegerField(primary_key=True)
    date = models.DateField()
    customer_id = models.ForeignKey(Customer , on_delete=models.CASCADE)
    invoice_pic = models.ImageField(upload_to='invoice/images',default="Not present")
    invoice_desc = models.CharField(max_length=500,default='')
    outstanding = models.IntegerField(default=None,null=True,blank=True)
    def __int__(self):
        return self.invoice_id

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE, related_name='profile')

    customer_id = models.ForeignKey(to=Customer , on_delete=models.CASCADE , null = True , blank = True)

def get_queryset(self):
    return Invoice.objects.filter(customer_id=self.request.user.get_profile.customer_id)


@receiver(post_save , sender=User)
def create_profile_for_user(sender , instance , created, **kwargs):
    if created:
        profile = Profile.objects.get_or_create(user=instance )
        profile.save()

post_save.connect(create_profile_for_user, sender=User)

class Wallet(models.Model):
    invoice_id = models.CharField(max_length=20,default='',null=True,blank=True)
    username = models.CharField(max_length=100,primary_key=True)
    email = models.CharField(max_length=500,default='')
    amount = models.IntegerField(null=True,blank=True)
    balance = models.IntegerField(null=True , blank=True)
    def __str__(self):
        return self.username
