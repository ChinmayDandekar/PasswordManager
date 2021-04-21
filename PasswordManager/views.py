from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from PasswordManager.models import Passwords
from cryptography.fernet import Fernet

import re

def checkEmail(email):
    
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if re.search(regex, email):
        return True
 
    else:
        return False

def isNull(n):
    if n == '':
        return True
    else:
        return False



def index(request):

    return render(request, 'index.html' )

def viewallsites(request):

    passs = Passwords.objects.all()
    # for pas in passs:
    #     pas.password= sdff
    
    return render(request, 'viewallsites.html' ,{'passs' : passs})

def addsite(request):

    if request.method == 'POST':
        site_name = request.POST['site-name']
        site_url = request.POST['site-url']
        username = request.POST['username']
        password = request.POST['password']
        user  = User.objects.get(username)
        key = user
        fernet = Fernet(key)
        password = fernet.encrypt(password.encode())
        

        if isNull(site_name) or isNull(site_url) or isNull(username) or isNull(password):
            messages.info(request, 'No information should be empty')
            return redirect('addsite')


        if username.isnumeric():
            phoneNo = username
            username = '-'
            email = '-'
        elif checkEmail(username):
            email = username
            phoneNo = '-'
            username = '-'
        else:
            phoneNo = '-'
            email = '-'

        password = Passwords.objects.create(
        username=username, password=password, email=email, site_name=site_name, site_url=site_url , phoneNo = phoneNo)
        password.save()
        messages.info(request,'Password Stored')
        return redirect('addsite')

    

    else:
        

       return render(request, 'add_site.html')