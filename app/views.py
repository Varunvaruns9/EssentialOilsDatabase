from django.shortcuts import render, HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required
from .models import EssentialOil, Metabolite, Through
import pandas as pd
import math


# View for the query page.
def index(request):
    oils_list = EssentialOil.objects.all()
    metabolites_list = Metabolite.objects.all()
    # For storing the retrieved results.
    result = {}
    if request.method == 'POST':
        # If submit button for oil was pressed-
        # Retrieve all related metabolites.
        if 'oil' in request.POST:
            result['oil'] = EssentialOil.objects.get(name=request.POST['oil'])
            result['metabolites'] = result['oil'].metabolites.all()
        # If submit button for metabolite was pressed-
        # Retrieve all related oils.
        if 'metabolite' in request.POST:
            result['metabolite'] = Metabolite.objects.get(name=request.POST['metabolite'])
            result['oils'] = result['metabolite'].essentialoil_set.all()
    return render(request, 'index.html', {'oils_list': oils_list, 'metabolites_list': metabolites_list, 'result': result})


# View for the csv submission page.
@staff_member_required
def load(request):
    data = pd.read_csv(request.FILES['csv'], skiprows=1)
    # Find the oil according to given information or create if it doesn't exist.
    oil,_ = EssentialOil.objects.get_or_create(name=request.POST['name'], abbr=request.POST['abbr'],
                                                scientific_name=request.POST['scientific_name'], family=request.POST['family'])
    for index, row in data.iterrows():
        if isinstance(row[0], float):
            continue
        # Find the metabolite according to given information or create if it doesn't exist.
        meta,_ = Metabolite.objects.get_or_create(name=row[0])
        # Create a relationship between them if it doesn't exist.
        through,_ = Through.objects.get_or_create(oil=oil, metabolite=meta, time=row[1], mzratio=row[3], identity=row[4],
                                                    relative_abundance1=row[5], relative_abundance2=row[6],
                                                    relative_abundance3=row[7], relative_abundance4=row[8])
    return HttpResponseRedirect('/admin/')
