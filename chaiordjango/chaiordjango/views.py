from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    # return HttpResponse("<h1>Welcome to Chai's Django Project: Home page</h1>")
    return render(request, "index.html")

def about(request):
    return HttpResponse("<h1>Welcome to Chai's Django Project: About page</h1>")

def contact(request):
    return render(request,"website/contactus.html")

def privacy(request):
    return render(request,'privacy/index.html')

