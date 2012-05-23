from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView, CreateView
from entry.models import Post,Comment

urlpatterns = patterns('entry.views',
    url(r'^$', 'test_view'),
    #url(r'^(?P<pk>\d+)/$', 'detail'),
    #url(r'^add/$', 'new'),
)
