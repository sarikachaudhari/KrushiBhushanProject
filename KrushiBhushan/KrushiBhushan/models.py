from django.db import models
from django.contrib.auth.models import User
from django.core.files import File  # you need this somewhere
import urllib

# Create your models here.

class Products(models.Model):
	product_name = models.CharField(unique=True,max_length=20,null=True)
	image = models.ImageField(upload_to='file/', blank=True)
	description = models.CharField(max_length=10000)

	def __unicode__(self):
		return self.product_name

class Image(models.Model):
	IMG_TYPES = (
		(1,'banner'),
		(2,'gallery'),
		)
	img_type = models.IntegerField(choices=IMG_TYPES)
	image = models.ImageField(upload_to='file/', blank=True)

	def __unicode__(self):
		return str(self.img_type)
