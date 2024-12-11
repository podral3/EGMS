import unittest
from utils import *
from datetime import datetime

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

if __name__ == '__main__':
    unittest.main()