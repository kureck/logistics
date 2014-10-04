# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
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
					destiny = direction['destiny']
					weight = direction['weight']
					Direction.objects.create(road_map=road_map, origin=origin, destiny=destiny, weight=weight)
			elif form.files:
				collection_list = ld.load_data_from_csv(form.files['csv_file'])
				road_map = form.save(commit=True)
				for direction in collection_list:
					origin = direction['origin']
					destiny = direction['destiny']
					weight = direction['weight']
					Direction.objects.create(road_map=road_map, origin=origin, destiny=destiny, weight=weight)
			else:
				form.save(commit=True)
			return maps(request)
		else:
			print form.errors
	else:
		form = RoadMapForm()
	return render_to_response('shortest_path/create_map.html', { 'form' : form }, context)