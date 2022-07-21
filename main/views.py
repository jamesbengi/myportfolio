from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Infor
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


# Create your views here.
def index(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        subject=name
        msg=message
        sender=email
        send_mail(subject,msg,sender,['jamesbengi21@gmail.com'],fail_silently=False)
        messages.success(request,"Message send succesfully")
        return redirect('/')
    return render(request,'index.html')

