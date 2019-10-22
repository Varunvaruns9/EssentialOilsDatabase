from django.shortcuts import render


def index(request):
    results = {}
    if request.method == 'POST':
        if 'plant' in request.POST:
            results = 
        else:
            results = 
    render(request, 'index.html', {})
