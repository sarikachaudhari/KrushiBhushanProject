import json
from django.http import HttpResponse
from .models import *
from django.http import JsonResponse
from django.shortcuts import render_to_response,render


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
	jsonobj = json.loads(request.body)
	print jsonobj

	products = Products.objects.all()

	data=[]
	for i in products:
		products_list={"product_id":i.id,"product_name":i.product_name,"product_description":i.description,"product_image":i.image}
		data.append(products_list)

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

