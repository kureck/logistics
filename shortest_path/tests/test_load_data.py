# -*- coding: utf-8 -*-
from shortest_path.lib.load_data import LoadData

CORRECT_VALUE = [{'origin': u'A', 'destination': u'B', 'weight': 10.0}, {'origin': u'B', 'destination': u'D', 'weight': 11.0}, {'origin': u'E', 'destination': u'A', 'weight': 12.0}]

def test_load_data_from_text_field_empty():
    ld = LoadData()
    value = u''
    assert ld.load_data_from_text_field(value) == u''

def test_load_data_from_text_field_comma():
    ld = LoadData()
    value = u'A,B,10\nB,D,11\nE,A,12'
    assert ld.load_data_from_text_field(value) == CORRECT_VALUE

def test_load_data_from_text_field_space():
    ld = LoadData()
    value = u'A B 10\nB D 11\nE A 12'
    assert ld.load_data_from_text_field(value) == CORRECT_VALUE

def test_load_data_from_csv():
    ld = LoadData()
    csv_file = open('file/test.csv')
    assert ld.load_data_from_csv(csv_file) == CORRECT_VALUE
