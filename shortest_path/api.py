from django.conf.urls import *
from tastypie.resources import ModelResource
from tastypie.utils import trailing_slash
from tastypie.serializers import Serializer
from .lib.graph import Graph
import simplejson as json
from .models import RoadMap

class RoadMapResource(ModelResource):
    class Meta:
        queryset = RoadMap.objects.all()
        resource_name = 'map'
        allowed_methods = ['get', 'post']
        serializer = Serializer(formats=['json'])

    def find_shortest_path(self, request, **kwargs):
        self.method_check(request, allowed=['post'])
        response = {}
        if request.body:
            params = json.loads(request.body)
            map_id = params['road_map']
            origin = params['origin']
            destination = params['destination']
            road_map = RoadMap.objects.get(id=map_id)
            map_directions = road_map.direction_set.all()
            g = Graph(map_directions)
            litro = float(params['litro'])
            autonomia = float(params['autonomia'])
            shortest_path_value = g.shortest_path_result(origin, destination, autonomia, litro)
            response['shortest_path_value'] = shortest_path_value['shortest_path_value']
            response['shortest_path'] = shortest_path_value['shortest_path']
        return self.create_response(request, response)


    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/find_shortest_path%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('find_shortest_path'), name="api_find_shortest_path"),
        ]