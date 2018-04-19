# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
	Name=models.CharField(max_length=30)
	Description=models.TextField(max_length=50)




	
class Product(models.Model):
	Categories=models.ForeignKey(Category,on_delete=models.CASCADE)
	Name=models.CharField(max_length=20)
	Image=models.FileField(upload_to='media/',null=True,blank=True)
	IDorSNO=models.IntegerField()
	Description=models.TextField(max_length=50)
	Price=models.IntegerField()
	NumbersAvailable=models.IntegerField()
