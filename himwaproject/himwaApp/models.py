from django.db import models

# Create your models here.
class Login2(models.Model):
    name = models.CharField(max_length=200, default='example')
    email = models.EmailField(max_length=50, default='example@gmail.com')
    phone_number = models.CharField(max_length=10,default='0700000001')
    password = models.CharField(max_length=25)
    bill = models.PositiveIntegerField(default=0.0)
    paid = models.PositiveIntegerField(default=0.0)
    january = models.PositiveIntegerField(default=0.0)
    february = models.PositiveIntegerField(default=0.0)
    march = models.PositiveIntegerField(default=0.0)
    