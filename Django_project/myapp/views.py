from django.shortcuts import render
from .models import Contact


# Create your views here.
def index(request):
	return render(request,'index.html')
def contact(request):
	if request.method=="POST":
		pass

	else:
		return render(request,'contact.html')
def signup(request):
	return render(request,'signup.html')
def login(request):
	return render(request,'login.html')

