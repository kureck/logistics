# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import RoadMap

def index(request):
  context = RequestContext(request)
  context_dict = { }
  return render_to_response('shortest_path/index.html', context_dict, context)