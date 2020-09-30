from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .models import EmailDetail, Message

# Create your views here.
def register(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		email = request.POST.get('email')
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')

		if password1 == password2:
			if User.objects.filter(email= email).exists():
				messages.info(request, "Email already exist")
				return redirect('/')
			elif User.objects.filter(username = username).exists():
				messages.info(request, "Username already exist")
				return redirect('/')
			else:
				user = User.objects.create_user(username=username, password=password2, first_name=first_name,
					   last_name=last_name,email=email)
				user.save()
				messages.info(request, "User Created")
				return render(request, 'login.html')
		else:
			messages.info(request, "Passwords doesn't match")
			return redirect('/')

	else:
		return render(request, 'register.html')

def login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username , password=password)

		if user is not None:
			auth.login(request, user)
			return render(request, 'home.html')
		else:
			messages.info(request, 'Invalid')
			return redirect('login')
	else:
		return render(request, 'login.html')

def logout(request):
	auth.logout(request)
	messages.info(request, "User logged out")
	return redirect('/')

def home(request):
	return render(request, 'home.html')

def details(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		name = request.POST.get('name')

		if EmailDetail.objects.filter(email = email).exists():
			messages.info(request, 'Email already exist in the list')
			return redirect('details')
		else:
			detail = EmailDetail(email= email, name= name)
			detail.save()
			messages.info(request, 'Email successfully added to the list')
			return render(request, 'home.html')
	else:
		return render(request, 'details.html')

def sendmsg(request):
	if request.method == 'POST':
		message = request.POST['message']
		name = request.POST['name']

		msg = Message(message = message, name = name)
		msg.save()
		messages.info(request, "Message has been saved to database")
		mail_subject = 'Important Message'
		body = render_to_string('Content_mail.html', {
					'user': 'Mr. xyz',
					'designation': 'abc',
					'Company': 'xyz Enterprises',
					'textmsg':message,})
		to_email = EmailDetail.objects.all().values_list('email')
		cd = [u[0] for u in to_email]
		mail = EmailMessage(mail_subject, body, to=cd )
		mail.send()
		messages.info(request, 'and send to given emails')
		return render(request, 'home.html')
	else:
		return render(request, 'sendmsg.html')

