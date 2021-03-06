# -*- coding: utf-8 -*-
import re
import csv

class LoadData:
    def load_data_from_text_field(self, text):
        if text:
            text = text.split('\n')
            values = [re.split(',| ',x) for x in text]
            collection_list = []
            for v in values:
                origin, destination, weight = v
                collection_list.append({ 'origin' : origin, 'destination' : destination, 'weight' : float(weight) })
            return collection_list
        else:
            return u''

    def load_data_from_csv(self, file_name):
        reader = csv.reader(file_name)
        collection_list = []
        for values in reader:
            origin, destination, weight = values
            collection_list.append({ 'origin' : unicode(origin), 'destination' : unicode(destination), 'weight' : float(weight) })
        return collection_list