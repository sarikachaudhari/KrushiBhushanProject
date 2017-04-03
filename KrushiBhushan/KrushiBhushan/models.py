from django.db import models
from django.utils import timezone

class Team(models.Model):
	employee = models.CharField(null=True,max_length=20)
	qulification = models.CharField(null=True,max_length=20)
	employee_pic = models.ImageField(null=True,max_length=20,blank=True)

 	def __unicode__(self):
		return str(self.employee) + '__' +  str(self.employee.id)

class Contact(models.Model):
	email = models.TextField(max_length=30,null=True)
	mobno = models.IntegerField(null=True,unique=True)
	
	def __unicode__(self):
		return str(self.email)

class Menu(models.Model):

	Home = models.CharField(null=True,max_length=2)
	about = models.CharField(null=True,max_length=2)
	Contact = models.CharField(null=True,max_length=2)
	Gallery = models.CharField(null=True,max_length=2)
	Product = models.CharField(null=True,max_length=2)

	def __unicode__(self):
		return str(self.Home)