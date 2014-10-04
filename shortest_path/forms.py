# -*- coding: utf-8 -*-
from django import forms
from .models import RoadMap

class RoadMapForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=128, label="Nome")
    csv_file = forms.FileField(label='Arquivo', required=False)
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='Direções', required=False)

    class Meta:
        model = RoadMap
        fields = ['name', 'text', 'csv_file']