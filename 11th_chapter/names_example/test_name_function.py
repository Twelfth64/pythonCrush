import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Test for name_function.py"""

    def test_first_last_name(self):
        """Are names like Jhon Doe formatted correctly?"""
        formatted_name = get_formatted_name('Jhon', 'Doe')
        self.assertEqual(formatted_name, 'Jhon Doe')


    def test_first_last_middle_name(self):
        """Are names like Jhon Body Doe formatted correctly?"""
        formatted_name = get_formatted_name('Jhon', 'Doe', 'Body')
        self.assertEqual(formatted_name, 'Jhon Body Doe')

if __name__ == '__main__':
    unittest.main()