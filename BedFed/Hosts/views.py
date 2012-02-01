# Create your views here.
from pyexpat import model
from django.shortcuts import render_to_response
import Hosts
from Hosts.models import Property

def search(request):
    #propertylist = Property.objects.all()
    error = False
    if 'search_terms' in request.GET and 'arrival_date' in request.GET and 'dept_date' in request.GET:
        search_terms = request.GET['search_terms']
        arrival_date = request.GET['arrival_date']
        dept_date = request.GET['dept_date']
        if not search_terms or not arrival_date or not dept_date:
            error = True
        else:
            #books = Book.objects.filter(title__icontains=q)
            properties = Property.objects.filter(city__icontains=search_terms)
            return render_to_response('search_results.html',
                    {'properties': properties, 'search_terms': search_terms })
    return render_to_response('home.html',{'error': error})

def home(request):
    return render_to_response('home.html')
