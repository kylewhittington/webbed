from django.contrib.auth.models import User
from Hosts.models import Invoice

__author__ = 'flipflop'

from BedFed.Hosts.models import User, Property, Booking, Review

from django.contrib import admin

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('addressline1', 'user')
    search_fields = ('postcode', 'addressline1')

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'join_date')
    list_filter = ('join_date',)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user','date','property')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'property', 'arrival_date')

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('booking', 'paid')

#admin.site.register(User, UserAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Invoice, InvoiceAdmin)