from django.shortcuts import render, HttpResponse
from .models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.


def index(request):
    context = {
        'variable': 'this is variable'
    }
    return render(request, 'index.html', context=context)


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('number')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, mobile=mobile, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'successfully updated!')
    return render(request, 'contact.html')

