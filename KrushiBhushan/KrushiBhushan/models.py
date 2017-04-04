from django.db import models
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


class Team(models.Model):
	employee = models.CharField(null=True,max_length=20)
	qualification = models.CharField(null=True,max_length=20)
	employee_pic = models.ImageField(upload_to='file/',null=True,blank=True)
		
	def __unicode__(self):
		return str(self.employee)
	
	
class Contact(models.Model):
	email = models.TextField(max_length=30,null=True)
	address = models.TextField(max_length=50,null=True)
	mobno = models.IntegerField(null=True,unique=True)
	
	def __unicode__(self):
		return str(self.email) + '_' + str(self.mobno) + '_' + str(self.address)
	

class Menu(models.Model):

	title = models.CharField(null=True,max_length=10)
	url = models.CharField(null=True,max_length=10)
	
	def __unicode__(self):
		return str(self.title)


