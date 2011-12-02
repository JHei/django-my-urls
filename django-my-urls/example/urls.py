# urls.py
from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic import ListView, CreateView, UpdateView
from myurls.models import MyUrl, Click
from example.views import MyUrlsList, api_create_myurl
from example.forms import CreateMyUrlForm, EditMyUrlForm

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^create/', CreateView.as_view(model=MyUrl,form_class=CreateMyUrlForm)),
    (r'^edit/(?P<id>)$', 
        UpdateView.as_view(model=MyUrl, form_class=EditMyUrlForm, 
            query_set=MyUrl.objects.get(pk__exact=myurl_id))),
    (r'^api/(?P<url>.*)', api_create_myurl),
    (r'^list$', ListView.as_view(model=MyUrl)),
)

urlpatterns = urlpatterns + patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    ) if settings.DEBUG else urlpatterson

