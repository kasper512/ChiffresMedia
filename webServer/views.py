from django.shortcuts 				import render
from django.contrib 				import auth
from django.contrib.auth 			import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models 	import User
from django.core.exceptions			import ObjectDoesNotExist

from .models import Message

# Create your views here.

def login(request):
	email 		= request.POST.get('email', 'gentoo@localhost')
	password	= request.POST.get('password', '1qaz@WSX')
	user 		= authenticate(username=email, password=password)

	print (email)
	print (password)
	print (user)

	if user is not None:
		if user.is_active:
			auth.login(request, user)

	return render(request, "login.xml", {})

@login_required()
def logout(request):
	auth.logout(request)
	return render(request, "logout.xml", {})

@login_required()
def getMessages(request):
	return render(request, "default.xml", {})

@login_required()
def sendMessage(request):
	text	= request.POST.get('text', 'example message :)')
	sender	= request.POST.get('sender', 'gentoo@localhost')
	
	msg = Message.objects.create()
	msg.UserFrom = User.objects.get(username='gentoo@localhost')
	msg.Text = text
	msg.save()
	
	return render(request, "default.xml", {})

@login_required()
def sendPublicKey(request):
	return render(request, "default.xml", {})