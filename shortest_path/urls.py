from django.conf.urls import patterns, url
from shortest_path import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^maps/$', views.maps, name='maps'),
	url(r'^maps/(?P<pk>\d+)/$', views.map_detail, name='map_detail'),
	url(r'^create_map/$', views.create_map, name='create_map'),
	url(r'^find_shortest_path/(?P<pk>\d+)/$', views.find_shortest_path, name='find_shortest_path'),
)