from django.shortcuts import render

# Create your views here.
def chai(request):
    return render(request,"chai/all_chai.html")
