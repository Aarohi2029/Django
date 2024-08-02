from django.shortcuts import render,redirect
from .models import User,Friend
from django.db.models import Q
# Create your views here.
def index(request):
	try:
		user=User.objects.get(email=request.session['email'])
		users=User.objects.filter(~Q(email=user.email))
		friends=Friend.objects.all()
		return render(request,'index.html',{'users':users,'friends':friends})
	except:
		return render(request,'index.html')


def signup(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			msg="Email Already Registered"
			return render(request,'signup.html',{'msg':msg})
		except:
			if request.POST['password']==request.POST['cpassword']:
				User.objects.create(
						fname=request.POST['fname'],
						lname=request.POST['lname'],
						email=request.POST['email'],
						mobile=request.POST['mobile'],
						password=request.POST['password'],
						profile_picture=request.FILES['profile_picture']
					)
				msg="User Sign Up Successfully"
				return render(request,'signup.html',{'msg':msg})
			else:
				msg="Password & Confirm Password Does Not Matched"
				return render(request,'signup.html',{'msg':msg})
	else:
		return render(request,'signup.html')

def login(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			if user.password==request.POST['password']:
				request.session['email']=user.email
				request.session['fname']=user.fname
				request.session['profile_picture']=user.profile_picture.url
				return redirect('index')
			else:
				msg="Incorrect Password"
				return render(request,'login.html',{'msg':msg})
		except Exception as e:
			print(e)
			msg="Email Not Registered"
			return render(request,'login.html',{'msg':msg})
	else:
		return render(request,'login.html')

def logout(request):
	try:
		del request.session['email']
		del request.session['fname']
		del request.session['profile_picture']
		return render(request,'login.html')
	except:
		return render(request,'login.html')

def add_friend(request,pk):
	user=User.objects.get(email=request.session['email'])
	friend=User.objects.get(pk=pk)
	Friend.objects.create(user=user,friend=friend,status=True)
	return redirect('index')
