import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        """Make an employee to use in tests."""
        self.richie = Employee('richie', 'wong', 90000)

    def test_give_default_raise(self):
        """Test that a default raise works correctly"""
        self.richie.give_raise()
        self.assertEqual(self.richie.salary, 95000)

    def test_give_custom_raise(self):
        """Test that a custom raise works correctly"""
        self.richie.give_raise(10000)
        self.assertEqual(self.richie.salary, 100000)

unittest.main()
