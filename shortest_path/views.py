# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404
from .models import RoadMap, Direction
from .forms import RoadMapForm
from .lib.load_data import LoadData
import ipdb

def index(request):
	context = RequestContext(request)
	context_dict = { }
	return render_to_response('shortest_path/index.html', context_dict, context)

def maps(request):
	context = RequestContext(request)
	maps = RoadMap.objects.all()
	context_dict = { 'maps' : maps }
	return render_to_response('shortest_path/maps.html', context_dict, context)

def map_detail(request, pk):
	context = RequestContext(request)
	try:
		road_map = RoadMap.objects.get(pk=pk)
		map_directions = road_map.direction_set.all()
		context_dict = { 'road_map' : road_map, 'map_directions' : map_directions }
	except RoadMap.DoesNotExist:
		raise Http404
	return render_to_response('shortest_path/map_detail.html', context_dict, context)

def create_map(request):
	context = RequestContext(request)
	if request.method == 'POST':
		form = RoadMapForm(request.POST, request.FILES)
		if form.is_valid():
			ld = LoadData()
			# ipdb.set_trace()
			if form.data['text']:
				collection_list = ld.load_data_from_text_field(form.data['text'])
				road_map = form.save(commit=True)
				for direction in collection_list:
					origin = direction['origin']
					destination = direction['destination']
					weight = direction['weight']
					Direction.objects.create(road_map=road_map, origin=origin, destination=destination, weight=weight)
			elif form.files:
				collection_list = ld.load_data_from_csv(form.files['csv_file'])
				road_map = form.save(commit=True)
				for direction in collection_list:
					origin = direction['origin']
					destination = direction['destination']
					weight = direction['weight']
					Direction.objects.create(road_map=road_map, origin=origin, destination=destination, weight=weight)
			else:
				form.save(commit=True)
			return maps(request)
		else:
			print form.errors
	else:
		form = RoadMapForm()
	return render_to_response('shortest_path/create_map.html', { 'form' : form }, context)

def find_shortest_path(request, pk):
	context = RequestContext(request)
	try:
		road_map = RoadMap.objects.get(pk=pk)
		map_directions = road_map.direction_set.all()
		origins = map_directions.values_list('origin', flat=True)
		destinations = map_directions.values_list('destination', flat=True)
		context_dict = { 'road_map' : road_map, 'map_directions' : map_directions, 'origins' : origins, 'destinations' :destinations }
	except RoadMap.DoesNotExist:
		raise Http404
	return render_to_response('shortest_path/find_shortest_path.html', context_dict, context)