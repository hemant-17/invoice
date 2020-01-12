from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save


# Create your models here.



class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=150)
    outstanding = models.IntegerField()
    def __str__(self):
        return self.customer_name

class Invoice(models.Model):
    invoice_id = models.IntegerField(primary_key=True)
    date = models.DateField()
    customer_id = models.ForeignKey(Customer , on_delete=models.CASCADE)
    invoice_pic = models.ImageField(upload_to='invoice/images',default="Not present")
    invoice_desc = models.CharField(max_length=500,default='')
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




class Order(models.Model):
    customer_id = models.ForeignKey(Customer , on_delete=models.CASCADE )
    invoice_no = models.ForeignKey(Invoice ,on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.IntegerField()
    class Meta:
        unique_together=(("customer_id","invoice_no"),)



class Payments(models.Model):
    customer_id = models.ForeignKey(Customer , on_delete=models.CASCADE  )
    invoice_no = models.ForeignKey(Invoice ,on_delete=models.CASCADE)
    pay_date = models.DateField()
    amount_paid = models.IntegerField()
    outstanding = models.IntegerField()
    class Meta:
        unique_together=(("customer_id","invoice_no"),)
