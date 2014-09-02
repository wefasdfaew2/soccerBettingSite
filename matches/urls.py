from django.conf.urls import patterns, url

from matches import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<match_id>\d+)/$', views.detail, name='detail'),
)
