import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """TESTS FOR 'name_function.py'."""

    def test_first_last_name(self):
        """DO NAMES LIKE 'Janis Joplin' WORK"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()
