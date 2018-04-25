import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):  # CREATE A CLASS THAT CONTAINS A SERIES OF UNIT TEST FOR FUNCTION
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')  # CALL FUNCTION YOU WANT TO TEST AND STORE A RETURN VALUE FOR TESTING
        self.assertEqual(formatted_name, 'Janis Joplin')    # ASSERT METTHOD --> VERIFIES THAT THE RESULT YOU RECEIVED MATCHES THE RESULT YOU EXPECTED TO RECEIVE

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()

# "." ON FIRST LINE --> TELLS US SINGLE TEST IS PASSED
# NEXT LINE --> TELLS USE HOW MANY TEST PYTHON RAN AND THE AMOUNT OF TIME IT TOOK
# "OK" ON LAST LINE --> TELLS US THAT ALL UNIT TESTS IN THE TEST CASE PASSED
