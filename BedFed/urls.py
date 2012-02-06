from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from Hosts import views
from BedFed import settings
import Hosts

admin.autodiscover()
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BedFed.views.home', name='home'),
    # url(r'^BedFed/', include('BedFed.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^search/', 'Hosts.views.search'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^weblog/', include('zinnia.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^contact/', 'Hosts.views.contact'),
#    url(r'^property/(\d{1,2})/(?P<ayear>\d{4})(?P<amonth>\d{2})(?P<aday>\d+)/(?P<dyear>\d{4})(?P<dmonth>\d{2})(?P<dday>\d+)/$', 'Hosts.property.views.view'),
    url(r'^property/(?P<propertyId>\d{1,2})/(?P<arrival_date>\d{8})/(?P<dept_date>\d{8})/$', 'Hosts.property.views.view'),
    url(r'^property/(\d{1,2})/book', 'Hosts.property.views.book'),
    #url(r'^weeklyreports/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d+)/$', 'weeklyreports'),
    url(r'$', 'Hosts.views.home'),
)
