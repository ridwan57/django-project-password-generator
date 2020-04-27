from django.http import HttpResponse
from django.shortcuts import render
import random

def home(request):
    return render(request,'calc/home.html',{'password':'df34t3fgrg'})


def password(request):
	
	thepassword = ''

	characters = list('abcdefghijklmnopqrstuvwxyz')

	if request.GET.get('uppercase'):
		characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

	if request.GET.get('special'):
		characters.extend(list('!@#$%^&*()'))

	if request.GET.get('numbers'):
		characters.extend(list('1234567890'))



	length = int(request.GET.get('length',12))

	for x in range(length):
		thepassword+=random.choice(characters)


	return render(request,'calc/password.html', {'password' :thepassword})


def about(request):
    return render(request,'calc/about.html')



