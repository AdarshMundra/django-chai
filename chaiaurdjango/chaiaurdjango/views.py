from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request, 'index.html')

def home1(request):
    return HttpResponse("<h1>Welcome to Chai's Django Project: Home page</h1>")

def about(request):
    return HttpResponse("<h1>Welcome to Chai's Django Project: about page</h1>")

def contact(request):
    return HttpResponse("<h1>Welcome to Chai's Django Project: contact page</h1>")

