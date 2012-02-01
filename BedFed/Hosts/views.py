# Create your views here.
from pyexpat import model
from django.shortcuts import render_to_response
import Hosts
from Hosts.models import Property

def search(request):
    propertylist = Property.objects.all()
    return render_to_response('search.html', locals())
    
def home(request):
    return render_to_response('home.html')
