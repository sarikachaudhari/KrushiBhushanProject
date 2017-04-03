from .models import *
import json
from django.http import HttpResponse

def AddTeam(request):
	jsonobj=json.loads(request.body)
    
	qulification = jsonobj.get("qulification")
	employee_pic = jsonobj.get('employee_pic')
	employee = jsonobj.get('employee') 

	try:
		team = Team()
		team.employee = employee
		team.qulification = qulification
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
						"qulification" : team.qulification,
						"employee_pic" : team.employee_pic

		}
		team_list.append(employee)
	return HttpResponse(json.dumps({"validation":"Team Details:","status":True,"team_list":repr(team_list)}), content_type="application/json")

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
	return HttpResponse(json.dumps({"validation":"Contact list Details:","status":True,"contact_detail ":contact_list}), content_type="application/json")

