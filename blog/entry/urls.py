from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView, CreateView
from entry.models import Post,Comment

urlpatterns = patterns('entry.views',
    url(r'^$', 'index_view', name='home'),
    url(r'^add/$', 'test_view'),
    url(r'^(?P<post_id>\d+)/$', 'detail_view', name="entry"),
    url(r'^(?P<post_id>\d+)/add/$', 'comment_view'),
)
