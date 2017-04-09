from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import os


# Create your views here.

def index(request):
	return HttpResponse("<h1> Hello World </h1>")

def problem(request):
	context = {}
	return render(request,'grading/problem.html', context)

def submit(request):
	fileName = request.POST['name']
	f = request.FILES['submission']
	with open("../submissions/"+fileName, 'wb') as destination:
		for chunk in f.chunks():
			destination.write(chunk)

	os.system("cd ../submissions \n python3 "+fileName)

	return HttpResponse(request.FILES['submission'].read())
