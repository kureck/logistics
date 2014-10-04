# -*- coding: utf-8 -*-
from django.db import models

class RoadMap(models.Model):
	name = models.CharField(max_length=128, unique=True)
	csv_file = models.FileField(upload_to='csv_files', blank=True)

	def __unicode__(self):
		return self.name

class Direction(models.Model):
	road_map = models.ForeignKey(RoadMap)
	origin = models.CharField(max_length=128)
	destination = models.CharField(max_length=128)
	weight = models.FloatField()

	def __unicode__(self):
		self.road_map