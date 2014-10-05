from django.conf.urls import *
from tastypie.resources import ModelResource
from tastypie.utils import trailing_slash
from tastypie.serializers import Serializer
from .models import RoadMap

class RoadMapResource(ModelResource):
    class Meta:
        queryset = RoadMap.objects.all()
        resource_name = 'map'
        allowed_methods = ['get', 'post']
        serializer = Serializer(formats=['json'])


    def find_shortest_path(self, request, **kwargs):
        self.method_check(request, allowed=['post','get'])
        response = {}
        if request:
            # Do the magic
            # shortest_path_value = do_the_magic(params)

            response['shortest_path_value'] = 10
            response['shortest_path'] = ['A', 'D', 'F']
            import ipdb; ipdb.set_trace()
        return self.create_response(request, response)


    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/find_shortest_path%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('find_shortest_path'), name="api_find_shortest_path"),
        ]