# Create your views here.
from pyexpat import model
import user
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
import Hosts
from Hosts.models import Property, ContactForm
from django.contrib import auth
from django.contrib.auth import logout
from django.template import RequestContext

def search(request):
    error = False
    if 'search_terms' in request.GET and 'arrival_date' in request.GET and 'dept_date' in request.GET:
        search_terms = request.GET['search_terms']
        arrival_date = request.GET['arrival_date']
        dept_date = request.GET['dept_date']
        if not search_terms or not arrival_date or not dept_date:
            error = True
        else:
            properties = Property.objects.filter(city__icontains=search_terms)
            return render_to_response('search_results.html',
                    {'properties': properties, 'search_terms': search_terms })
    return render_to_response('home.html',{'error': error}, context_instance=RequestContext(request, processors=[custom_proc]))

def home(request):
    return render_to_response('home.html', context_instance=RequestContext(request, processors=[custom_proc]))

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return render_to_response('contact/thanks.html')
    else:
        form = ContactForm()
    return render_to_response('contact/contact_form.html',{'form': form}, context_instance=RequestContext(request))

def custom_proc(request):
    return {
        'user': request.user,
        }
