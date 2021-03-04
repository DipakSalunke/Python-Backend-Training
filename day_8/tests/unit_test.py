import unittest
from doc_test import fizzbuzz

class test_fizzbuzz(unittest.TestCase):
    def test1(self):
        self.assertEqual(fizzbuzz(15), "fizzbuzz")

    def test2(self):
        self.assertEqual(fizzbuzz(29), 29)
    
    @unittest.skip("idr")
    def test2(self):
        self.assertEqual(fizzbuzz(20), "buzz")
if __name__ == '__main__':
    unittest.main()