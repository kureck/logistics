# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import RoadMap
from .forms import RoadMapForm
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
		form = RoadMapForm(request.POST)
		if form.is_valid():
			# ipdb.set_trace()
			form.save(commit=True)
			return maps(request)
		else:
			print form.errors
	else:
		form = RoadMapForm()
	return render_to_response('shortest_path/create_map.html', { 'form' : form }, context)