# from multiprocessing import context
from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import render
from datetime import datetime
from Home.models import Contact
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, surname=surname ,email=email , phone=phone ,desc=desc , date=datetime.today())
        contact.save()
        messages.success(request, 'Your Message Has Been Sent Successfully!')
    return render(request, "contact.html")
