from django.db import models

# Create your models here.



class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=150)
    outstanding = models.IntegerField()

class Invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    #invoice_pic = models.ImageField(upload_to='invoice/images',default="Not present")
    invoice_desc = models.CharField(max_length=500,default='')

<<<<<<< HEAD
class Order(models.Model):
=======
 class Order(models.Model):
>>>>>>> 94e67deaddb59615b1749ffdfcdb3285bb11d8b3
    customer_id = models.ForeignKey(Customer , on_delete=models.CASCADE )
    invoice_no = models.ForeignKey(Invoice ,on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.IntegerField()
    class Meta:
        unique_together = (("customer_id", "invoice_no"),)

<<<<<<< HEAD
class Payments(models.Model):
=======
 class Payments(models.Model):
>>>>>>> 94e67deaddb59615b1749ffdfcdb3285bb11d8b3
    customer_id = models.ForeignKey(Customer , on_delete=models.CASCADE )
    invoice_no = models.ForeignKey(Invoice ,on_delete=models.CASCADE)
    pay_date = models.DateField()
    amount_paid = models.IntegerField()
    outstanding = models.IntegerField()
    class Meta:
<<<<<<< HEAD
        unique_together = (("customer_id", "invoice_no"),)
=======
        unique_together = (("customer_id", "invoice_no"),)
>>>>>>> 94e67deaddb59615b1749ffdfcdb3285bb11d8b3
