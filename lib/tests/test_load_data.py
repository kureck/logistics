# -*- coding: utf-8 -*-
from lib.load_data import LoadData

def test_remove_dollar_sign():
    ld = LoadData()
    value = u''
    assert ld.load_data_from_text_field(value) == u''