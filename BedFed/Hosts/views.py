# Create your views here.
from pyexpat import model
import user
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
import Hosts
from Hosts.models import Property
from django.contrib import auth
from django.contrib.auth import logout
from django.template import RequestContext

def custom_proc(request):
    "A context processor that provides 'app', 'user' and 'ip_address'."
    return {
        'user': request.user,
    }


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
    return render_to_response('home.html',{'error': error}, context_instance=RequestContext(request, processors=[custom_proc]))

def home(request):
    return render_to_response('home.html', context_instance=RequestContext(request, processors=[custom_proc]))

#def login_view(request):
#    username = request.POST.get('username', '')
#    password = request.POST.get('password', '')
#    user = auth.authenticate(username=username, password=password)
#    if user is not None and user.is_active:
#        # Correct password, and the user is marked "active"
#        auth.login(request, user)
#        # Redirect to a success page.
#        return HttpResponseRedirect("/")
#    else:
#        # Show an error page
#        return HttpResponseRedirect("/account/invalid/")
#
#def logout_view(request):
#    logout(request)
#    return HttpResponseRedirect("/")