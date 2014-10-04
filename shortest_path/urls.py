from django.conf.urls import patterns, url
from shortest_path import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
)