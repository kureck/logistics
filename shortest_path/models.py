# -*- coding: utf-8 -*-
from django.db import models

class RoadMap(models.Model):
	name = models.CharField(max_length=128, unique=True)
	origin = models.CharField(max_length=128, unique=True)
	destiny = models.CharField(max_length=128, unique=True)
	weight = models.FloatField()

	def __unicode__(self):
		return self.name