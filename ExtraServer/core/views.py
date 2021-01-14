from django.shortcuts import render
from django.views import View
from django.core import serializers
from django.http import JsonResponse
import json
import os

# Create your views here.



def home(request, *args, **kwargs):
	template_name='index.html'
	context = {}
	return render(
		request,
		template_name,
		context,
	)


def button_clicked(request, *arga, **kwargs):
	# btnId = request.GET.get('btnId')

	data = json.loads(request.body)
	btnId = data['btnId']
	print(btnId)


	if btnId == "1":
		print("ls: ", os.system("ls"))
		pass
	elif btnId == "2":
		pass
	elif btnId == "3":
		pass
	elif btnId == "4":
		pass

	return JsonResponse("Done", safe=False, status=200)