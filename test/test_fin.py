import unittest
from datetime import date

import fin


class BasicTest(unittest.TestCase):
    def test_xirr(self):

        test_dates = [date(2010, 12, 29), date(2012, 1, 25), date(2012, 3, 8)]
        test_values = [-10000, 20, 10100]

        result = 0.010061265164920336

        self.assertEqual(fin.xirr(test_dates, test_values), result)

if __name__ == '__main__':
    unittest.main()
