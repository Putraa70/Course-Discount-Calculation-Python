import unittest
import pandas as pd
from hitung_total import hitung_total

class TestHitungTotal(unittest.TestCase):
    def setUp(self):
        # Siapkan data dummy untuk pengujian
        self.data = {
            'Courses': 'Python',
            'Categories': 'PI',
            'Fee': 20000,
            'Duration': 40,
            'Percentage Discount': 10
        }
        self.row = pd.Series(self.data)

    def test_hitung_total(self):
        result = hitung_total(self.row)
        expected_result = (20000 * 40) - (20000 * 40 * 0.10) - ((20000 * 40 * 0.10) * 0.02)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()


