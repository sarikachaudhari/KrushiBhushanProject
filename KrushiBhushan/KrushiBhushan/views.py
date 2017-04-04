from .models import *
import json
from django.http import HttpResponse
from django.http import JsonResponse


def add_product(request):
	jsonobj = json.loads(request.body)
	print jsonobj

	pro_name = jsonobj.get('proName')
	pro_image = jsonobj.get('proImage')
	pro_description = jsonobj.get('proDescription')

	if pro_name==None:
		return HttpResponse(json.dumps({"status":False,"validation":'Enter Product Name'}), content_type="application/json")

	product = Products(product_name = pro_name,image = pro_image,description = pro_description)
	product.save()
	return HttpResponse(json.dumps({"status":True,"validation":'Product added successfully'}), content_type="application/json")


def get_all_products(request):
	jsonobj=json.loads(request.body)
    
	print jsonobj

	products = Products.objects.all()

	data=[]
	for i in products:
		products_list={"product_id":i.id,"product_name":i.product_name,"product_description":i.description,"product_image":i.image.url}
		data.append(products_list)
	print data
	return HttpResponse(json.dumps({"status":True, "product_list":data}), content_type="application/json")



def slider(request):
	jsonobj = json.loads(request.body)
	print jsonobj

	slider_images = Image.objects.filter(img_type = 1)
	data=[]
	for i in slider_images:
		image = {"image":i.image.url}
		data.append(image)
	print data
	return HttpResponse(json.dumps({"status":True, "image_list":data}), content_type="application/json")


def gallery(request):
	jsonobj = json.loads(request.body)
	print jsonobj

	gallery_images = Image.objects.filter(img_type = 2)
	data=[]
	for i in gallery_images:
		image = {"image":i.image.url}
		data.append(image)
	print data
	return HttpResponse(json.dumps({"status":True, "image_list":data}), content_type="application/json")



def AddTeam(request):
	jsonobj=json.loads(request.body)
    
	qualification = jsonobj.get("qualification")
	employee_pic = jsonobj.get('employee_pic')
	employee = jsonobj.get('employee') 

	try:
		team = Team()
		team.employee = employee
		team.qualification = qualification
		team.employee_pic = employee_pic
		team.save()
		return HttpResponse(json.dumps({"validation":"Team registraction is succefully","status":True}), content_type="application/json")
	except Exception as e:
		print e
		return HttpResponse(json.dumps({"validation":"Team registraction is failed","status":False}), content_type="application/json")


def get_team(request):
	teams = Team.objects.all()

	team_list = []
	for team in teams:
		print team
	
		employee = {	"employee":team.employee,
						"qualification" : team.qualification,
						"employee_pic" : team.employee_pic.url

		}
		team_list.append(employee)
	print ('********************'),team_list
	return HttpResponse(json.dumps({"validation":"Team Details:","status":True,"team_list":team_list}), content_type="application/json")

def add_contact(request):
	jsonobj = json.loads(request.body)

	email=jsonobj.get("email")
	mobno=jsonobj.get("mobno")
	address=jsonobj.get("address")

	try:
		contacts = Contact()
		contacts.email=email
		contacts.mobno=mobno
		contacts.address=address
		contacts.save()
		print contacts
		return HttpResponse(json.dumps({"validation":"Contacts details register succefully","status":True}), content_type="application/json")
	except Exception as e:
		print e
		return HttpResponse(json.dumps({"validation":"Contacts details registration is Failed" ,"status":False}), content_type="application/json")

def get_contact(request):
	contacts=Contact.objects.all()

	contact_list = []
	for contact in contacts:
		print contact
		
		contact_detail = {	"email":contact.email,
						"mobno" : contact.mobno,
						"address" : contact.address

		}
		contact_list.append(contact_detail)
	return HttpResponse(json.dumps({"validation":"Contact list Details:","status":True,"contact_detail":contact_list}), content_type="application/json")

