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
    #availability = models.ForeignKey(Availability)
    def __unicode__(self):
        return u'%s - %s' % (self.user.first_name, self.addressline1)

RATING = {
    1:'Poor',
    2:'Average',
    3:'Amazing'
}

class Review(models.Model):
    property = models.ForeignKey(Property)
    user = models.ForeignKey(User)
    date = models.DateTimeField('date reviewed')
    rating = models.IntegerField(choices=RATING.items(),default=3)
    text = models.TextField(max_length=5000,blank=True)

class Booking(models.Model):
    user = models.ForeignKey(User)
    property = models.ForeignKey(Property)
    arrival_date = models.DateTimeField('arrival date')
    dept_date = models.DateTimeField('departure date')
    #invoice = models.ForeignKey(Invoice)

class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea)
