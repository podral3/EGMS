import unittest
from utils import *
from datetime import datetime
from pandas import DataFrame

class utils_tests(unittest.TestCase):

    def test_date_is_parsed(self):
        date = parse_to_date("20180213")
        dt = datetime(2018, 2, 13)
        self.assertEqual(date,dt)
    
    def test_dates_are_matched(self):
        asc = "20180101"
        dsc = ["20180102","20180105"]
        d = {}
        d[asc] = dsc
        self.assertEqual(d, match_dates([asc],dsc,6))
    
    def test_further_dates_are_omitted(self):
        asc = "20180101"
        dsc = ["20180102","20180105", "20240101"]
        d = {}
        d[asc] = ["20180102","20180105"]
        self.assertEqual(d, match_dates([asc],dsc,6))
    
    def test_previous_dates_are_omitted(self):
        asc = "20180101"
        dsc = ["20170202", "20180102","20180105"]
        d = {}
        d[asc] = ["20180102","20180105"]
        self.assertEqual(d, match_dates([asc],dsc,6))

    #nn
    
    def test_finds_nearest(self):
        asc_tuple = (1,1)
        dsc_points = [
            ['u', 2,2],
            ['t', 10, 10],
            ['z', 1.5, 1.5]
        ]
        df = DataFrame(dsc_points, columns=['pid', 'latitude', 'longitude'])
        nn = nearest_neighbour(asc_tuple, df, 1)
        self.assertEqual(nn[0], 2)

    #radius

    def test_radius(self):
        asc_cords = (5,5)
        radius = 2
        dsc_points = [
            ['q', 4, 4],
            ['w', 4, 5],
            ['e', 1, 1]
        ]
        df = DataFrame(dsc_points, columns=['pid', 'latitude', 'longitude'])
        #nn = find_by_radius(asc_cords, df, radius)
        #self.assertEqual(len(nn), 2)
        

if __name__ == '__main__':
    unittest.main()