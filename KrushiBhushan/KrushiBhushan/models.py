from django.db import models


class Team(models.Model):
	employee = models.CharField(null=True,max_length=20)
	qulification = models.CharField(null=True,max_length=20)
	employee_pic = models.ImageField(null=True,blank=True)

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
	
	def __unicode__(self):
		return str(self.title)