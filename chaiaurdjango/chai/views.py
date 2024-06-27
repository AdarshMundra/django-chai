from django.shortcuts import render, get_object_or_404
from .models import ChaiVarity, Store
from .forms import ChaiVarietyForm
# Create your views here.


def chai(request):
    chais = ChaiVarity.objects.all()
    print(chais)
    return render(request, "chai/all_chai.html", {'chais': chais})


def chai_details(request, chai_id):
    chai = get_object_or_404(ChaiVarity, pk=chai_id)
    return render(request, 'chai/chai-details.html', {'chai': chai})


def chai_store_view(request):
    stores = None
    if request.method == 'POST':
        form = ChaiVarietyForm(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data['chai_variety']
            stores = Store.objects.filter(chai_variety=chai_variety)
    else:
        form = ChaiVarietyForm()

    return render(request, 'chai/chai_store.html', {'form': form, 'stores': stores})
