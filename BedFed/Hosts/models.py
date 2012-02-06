from django.db import models
from django.contrib.auth.models import User
from django import forms

class Property(models.Model):
    user = models.ForeignKey(User)
    addressline1 = models.CharField('address line 1',max_length=200)
    addressline2 = models.CharField('address line 2',max_length=200,blank=True)
    city = models.CharField(max_length=50)
    postcode = models.CharField(max_length=7)
    short_desc = models.TextField('short description',max_length=400)
    long_desc = models.TextField('long description',max_length=5000)
    heading = models.CharField('search heading',max_length=50)
    price = models.FloatField('price per person per night',default=35.00,)
    #availability = models.ForeignKey(Availability)
    def __unicode__(self):
        return u'%s - %s' % (self.user.first_name, self.addressline1)

RATING = {
    1:'Poor',
    2:'Average',
    3:'Amazing'
}

PAYMENT_METHOD = {
    0:'Mastercard',
    1:'Visa',
    2:'Bank transfer',
    3:'PayPal',
}

class Review(models.Model):
    property = models.ForeignKey(Property)
    user = models.ForeignKey(User)
    date = models.DateTimeField('date reviewed')
    rating = models.IntegerField(choices=RATING.items(),default=3)
    text = models.TextField(max_length=5000,blank=True)

class Booking(models.Model):
    date = models.DateTimeField()
    user = models.ForeignKey(User)
    property = models.ForeignKey(Property)
    arrival_date = models.DateField('arrival date')
    dept_date = models.DateField('departure date')
    #invoice = models.ForeignKey(Invoice)

class Invoice(models.Model):
    booking = models.ForeignKey(Booking)
    paid = models.BooleanField()
    payment_value = models.FloatField('payment')
#    payment_method = PAYMENT_METHOD

class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea)

class PaymentForm(forms.Form):
    fullname = forms.CharField(label='Name (as it appears on card)')
    addressline1 = forms.CharField(label='Address Line 1')
    addressline2 = forms.CharField(label='Address Line 2')
    email = forms.CharField(label='E-mail')
    ccnumber = forms.CharField(label='Card Number', max_length=16)
    ccexpiry = forms.CharField(label='Expiry Date (mmyy)', max_length=4)
    cccvc = forms.CharField(label='CVC Number', max_length=3)

