from django.db import models
class Category(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50, blank = False)

class Product(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=50, blank = False)
    catid = models.ForeignKey(Category,on_delete=models.CASCADE, blank = False)
    stock = models.IntegerField(blank = False)

class User(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, blank = False)
    email = models.CharField(max_length=50, blank = False)

class Orders(models.Model):
    id = models.AutoField(primary_key = True)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    productid = models.ForeignKey(Product, on_delete=models.CASCADE)