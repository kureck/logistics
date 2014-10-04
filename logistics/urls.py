from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'logistics.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),
	url(r'^$', include('shortest_path.urls', namespace="shortest_path")),
	url(r'^admin/', include(admin.site.urls)),
)
