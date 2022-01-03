from django.shortcuts import render,redirect

from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from .forms import *
# Create your views here.

# homepage

@login_required(login_url='login')

def home(request):
	return render(request,'home.html')

# login
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request,username=username,password=password)

		if user is not None:
			auth_login(request,user)
			return redirect('home')

		else:
			messages.info(request,'username or password is incorrect!')

	return render(request,'login.html')

# register
def registerPage(request):

	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')

			messages.success(request, 'Account successfully created for' + username)
		return redirect('home')

	context ={'form':form}


	return render(request,'register.html',context)


def logoutUser(request):
	logout(request)
	return redirect('login')