from django.shortcuts import render, HttpResponseRedirect
from .models import EssentialOil, Metabolite, Through


def index(request):
    oils_list = EssentialOil.objects.all()
    metabolites_list = Metabolite.objects.all()
    result = {}
    if request.method == 'POST':
        if 'oil' in request.POST:
            result['oil'] = EssentialOil.objects.get(name=request.POST['oil'])
            result['metabolites'] = result['oil'].metabolites.all()
        if 'metabolite' in request.POST:
            result['metabolite'] = Metabolite.objects.get(name=request.POST['metabolite'])
            result['oils'] = result['metabolite'].essentialoil_set.all()
    return render(request, 'index.html', {'oils_list': oils_list, 'metabolites_list': metabolites_list, 'result': result})

def load(request):
    print(request.FILES['csv'])
    return HttpResponseRedirect('/admin/')
