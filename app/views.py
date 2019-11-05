from django.shortcuts import render, HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required
from .models import EssentialOil, Metabolite, Through
import pandas as pd
import math


def index(request):
    """
    View for the query page. Loads all possible values of EssentialOils and Metabolites from the database and
    return the relationship between the selected EssentialOil and Metabolites and its corresponding matches.
    """
    oils_list = EssentialOil.objects.all().order_by('name')
    metabolites_list = Metabolite.objects.all().order_by('name')
    # For storing the retrieved results.
    result = {}
    if request.method == 'POST':
        # If submit button for oil was pressed-
        # Retrieve all related metabolites.
        if 'oil' in request.POST:
            result['oil'] = EssentialOil.objects.get(name=request.POST['oil'])
            result['metabolites'] = Through.objects.filter(oil=result['oil']).order_by('metabolite__name')
            # for metabolite in result['metabolites']:
            #     through['metabolite'] = Through.objects.get()
        # If submit button for metabolite was pressed-
        # Retrieve all related oils.
        if 'metabolite' in request.POST:
            result['metabolite'] = Metabolite.objects.get(name=request.POST['metabolite'])
            result['oils'] = Through.objects.filter(metabolite=result['metabolite']).order_by('oil__name')
    return render(request, 'index.html', {'oils_list': oils_list, 'metabolites_list': metabolites_list, 'result': result})


@staff_member_required
def load(request):
    """
    View for the csv submission page. Adds a new EssentialOil and related oils from the given CSV file.
    """
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


def manual(request):
    """
    View for rendering the user manual. Contains information on how to use and information about the authors.
    """
    return render(request, 'manual.html')
