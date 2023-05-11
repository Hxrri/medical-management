from django.db import models

# Create your models here.
class contact(models.Model):
    ename=models.CharField(max_length=30)
    phno=models.IntegerField()
    email=models.EmailField()
    address=models.TextField()


class product(models.Model):
    Pname=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.CharField(max_length=100)
    pimage=models.CharField(max_length=600)

class Order(models.Model):
    Oname=models.CharField(max_length=20)
    email=models.EmailField()
    items=models.CharField(max_length=30)
    address=models.TextField()
    price=models.IntegerField()
    quantity=models.IntegerField()
    poheno=models.IntegerField()
    delivery=models.BooleanField(default=False)



