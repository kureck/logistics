from django.conf.urls import patterns, url
from shortest_path import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^maps/$', views.maps, name='maps'),
	url(r'^create_map/$', views.create_map, name='create_map'),
)