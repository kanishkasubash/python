import unittest
import stringutil

class TestStringUtil(unittest.TestCase):
    
    def test_count_strings_by_character(self):
        names = ["Apple", "orange", "banana", "avocado"]
        count = stringutil.count_strings_by_character(names, 'A')
        self.assertEqual(count, 2)
    
    def test_count_strings_by_character_with_empty_strings(self):
        names = ["Apple", "orange", " ", "banana", "avocado"]
        count = stringutil.count_strings_by_character(names, 'A')
        self.assertEqual(count, 2)

if __name__ == '__main__':
    unittest.main()