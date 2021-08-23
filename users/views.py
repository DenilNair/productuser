
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from authentication import  context_processors

# Create your views here.

def profile(request):
    print('hello from profile')
    
    if context_processors.dict["testme"] == 'loggedin':
            
            
            return render(request,'profile.html',{'name':context_processors.dict["name"]})
    else:
            messages.info(request,'Invalid Credentials')
            return render(request,'home.html',{'name':'home '})
    
