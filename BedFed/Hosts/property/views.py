# Create your views here.
from datetime import datetime
from pyexpat import model
import user
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
import Hosts
from Hosts.models import Property, ContactForm, PaymentForm
from django.contrib import auth
from django.contrib.auth import logout
from django.template import RequestContext

def view(request, propertyId, arrival_date, dept_date):
    property = Property.objects.get(id=propertyId)
    arrival_date = datetime.strptime(arrival_date, "%Y%m%d")
    dept_date = datetime.strptime(dept_date, "%Y%m%d")
    nights = (dept_date - arrival_date).days
    booking_cost = "%.2f" % (property.price * nights)
    return render_to_response('property/view.html', locals())

def book(request, propertyId):
    property = Property.objects.get(id=propertyId)
    paymentform = PaymentForm()
    if request.method=='POST':
        return render_to_response('property/booking_complete.html', locals())
    return render_to_response('property/booking.html', locals(), context_instance=RequestContext(request))
