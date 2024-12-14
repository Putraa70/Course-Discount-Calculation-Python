import unittest
from hitung_total import hitung_total

class TestHitungTotal(unittest.TestCase):
    def test_kategori_pi(self):
        row = {'Fee': 20000, 'Duration': 30, 'Percentage Discount': 5, 'Categories': 'PI'}
        expected = 570000
        self.assertAlmostEqual(hitung_total(row), expected)

    def test_kategori_ds(self):
        row = {'Fee': 20000, 'Duration': 30, 'Percentage Discount': 5, 'Categories': 'DS'}
        expected = 570000
        self.assertAlmostEqual(hitung_total(row), expected)

    def test_data_tidak_valid(self):
        row = {'Fee': 'abc', 'Duration': '30', 'Percentage Discount': 5, 'Categories': 'PI'}
        self.assertIsNone(hitung_total(row))

    def test_kolom_hilang(self):
        row = {'Fee': 20000, 'Percentage Discount': 5, 'Categories': 'PI'}
        self.assertIsNone(hitung_total(row))

if __name__ == '__main__':
    unittest.main()
