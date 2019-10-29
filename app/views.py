from django.shortcuts import render, HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required
from .models import EssentialOil, Metabolite, Through
import pandas as pd
import math


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


@staff_member_required
def load(request):
    data = pd.read_csv(request.FILES['csv'], skiprows=1)
    oil,_ = EssentialOil.objects.get_or_create(name=request.POST['name'], abbr=request.POST['abbr'],
                                                scientific_name=request.POST['scientific_name'], family=request.POST['family'])
    for index, row in data.iterrows():
        if isinstance(row[0], float):
            continue
        meta,_ = Metabolite.objects.get_or_create(name=row[0])
        through,_ = Through.objects.get_or_create(oil=oil, metabolite=meta, time=row[1], mzratio=row[3], identity=row[4],
                                                    relative_abundance1=row[5], relative_abundance2=row[6],
                                                    relative_abundance3=row[7], relative_abundance4=row[8])
    return HttpResponseRedirect('/admin/')
