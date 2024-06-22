from django.shortcuts import render
from .models import ChaiVarity
# Create your views here.
def chai(request):
    chais = ChaiVarity.objects.all()
    print(chais)
    return render(request,"chai/all_chai.html",{'chais':chais})
