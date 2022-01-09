""" Testing experiments"""

import pytest 
from unittest.mock import Mock

@pytest.fixture
def map_master_product_id_product_id():
    return {
    "2001": 1,
    "2002": 2,
    "2003": 3,
    "2004": 4,
    "2005": 5,
    "2006": 6,
    "2007": 7,
    "2008": 8,
    "2009": 9,
    "20010": 10,
    "20011": 11,
    "20012": 12,
    "20013": 13,
    "20014": 14,
    "20015": 15,
    "20016": 16,
    "20017": 17,
    "20018": 18,
    "20019": 19,
    "20020": 20,
}



class DataGenerator:

    def __init__(self, data) -> None:
        self.data = data

    def generate_data(self):
        r = next(self.data, None)
        while r:
            yield r 
            r = next(self.data, None)
        return r

    def fetch_one(self):
        return next(self.generate_data(), None)
    


def map_products_ocurrences(cur, mapping):
    ret = cur.fetchone()
    data = {}

    while ret is not None:
        pa, pb, co_occ = ret
        pa = int(pa)
        pb = int(pb)
        pa = mapping[f'{pa}'] if f'{pa}' in mapping.keys() else pa
        pb = mapping[f'{pb}'] if f'{pb}' in mapping.keys() else pb
        co_occ = int(co_occ)
        if pa not in data.keys():
            data[pa] = {}
        if pb in data[pa].keys():
            data[pa][pb] += co_occ
        else:
            data[pa][pb] = co_occ
        ret = cur.fetchone()

    return data


@pytest.mark.parametrize("test_input,expected", [
    (iter([
        (2001,2002,1),
        (2001,2003,1),
        (2006,2007,7),
        (2005,2008,1),
        (20020,20010,1),
        (2001,2008,1),
        (20019,2005,5),
        (2004,2005,5),
    ]), {
        1: {
            2: 1,
            3: 1,
            8: 1,
        },
        6: {
            7: 7,
        },
        5: {
            8: 1,
        },
        20: {
            10: 1,
        },
        19: {
            5: 5
        },
        4: {
            5: 5,
        },
    }), 
])
def test_data(test_input, expected, map_master_product_id_product_id):
    dg = DataGenerator(test_input)
    mycursor = Mock(name="mycursor")
    mycursor.fetchone = dg.fetch_one
    data = map_products_ocurrences(mycursor, map_master_product_id_product_id)
    for k in expected.keys():
        r_data = data[k]
        e_data = expected[k]
        for k, v in r_data.items():
            assert e_data[k] == v
        for k, v in e_data.items():
            assert r_data[k] == v
    for k in data.keys():
        r_data = data[k]
        e_data = expected[k]
        for k, v in r_data.items():
            assert e_data[k] == v
        for k, v in e_data.items():
            assert r_data[k] == v


