from django.conf.urls import patterns, include, url
from avr.view import main,avr
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',url('^$', main),url('^avr$',avr),
    # Examples:
    # url(r'^$', 'testit.views.home', name='home'),
    # url(r'^testit/', include('testit.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
