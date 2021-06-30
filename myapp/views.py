from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Message

# Create your views here.
def homepage(request):
    if request.method == "POST":
        message = request.POST.get('message')
        homepage = Message(message_me=message, message_published=datetime.now())
        homepage.save()
    return render(request, 'index.html')
    #return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("this is about page")

def contact(request):
    return render(request, 'contact.html')
    #return HttpResponse("contacts")