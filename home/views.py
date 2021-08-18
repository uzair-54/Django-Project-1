from django.shortcuts import render, HttpResponse, resolve_url
from datetime import datetime
from home.models import Contact
from django.contrib import messages


# Create your views here.

def index(request):
    # return HttpResponse("THIS IS HOME PAGE")
    context = {
        'variable': '4532513'
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        date = datetime.today()
        cnt = Contact(name=name, email=email,
                      phone=phone, desc=desc, date=date)
        cnt.save()
        messages.success(request,"Your message has been recived we will contact you soon")
        
    return render(request, 'contact.html')

def development(request):
    return render(request, 'development.html')

def courses(request):
    return render(request, 'courses.html')

def game(request):
    return render(request,"game.html")

def web(request):
    return render(request,"web.html")

def ml(request):
    return render(request,"ml.html")
