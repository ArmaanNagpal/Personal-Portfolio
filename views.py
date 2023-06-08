from django.shortcuts import render,redirect
from portapp.models import contactform

# Create your views here.

def index(request):
	if request.method=='POST':
		x=contactform()
		x.fName=request.POST.get('fname')
		x.lName=request.POST.get('lname')
		x.email=request.POST.get('email')
		x.sub=request.POST.get('sub')
		x.msg=request.POST.get('msg')
		x.save()
		return render(request,'index.html',{'msg':1})
	else:
		return render(request,'index.html')

def projects(request):
	if request.method=='POST':
		x=contactform()
		x.fName=request.POST.get('fname')
		x.lName=request.POST.get('lname')
		x.email=request.POST.get('email')
		x.sub=request.POST.get('sub')
		x.msg=request.POST.get('msg')
		x.save()
		return render(request,'projects.html',{'msg':1})
	else:
		return render(request,'projects.html')