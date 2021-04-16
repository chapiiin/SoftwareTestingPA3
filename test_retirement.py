import unittest
from retirement import calculate_retirement
from bmi import calculate_bmi

class TestRetirement(unittest.TestCase):
##    def test_a_retirement_valid_input(self):
##        with self.assertRaises(ValueError) as exception_error:
##            actual = calculate_retirement('string', 'string', 'string', 'string')
##            self.assertEqual(actual, exception_error)

    def test_b_retirement_goal_met(self):
        actual = calculate_retirement(25, 70000, 10.5, 500000)
        expected = [76, True]
        self.assertEqual(actual, expected)
        
    def test_c_retirement_goal_met(self):
        actual = calculate_retirement(25, 70000, 10.5, 9000)
        expected = [26, True]
        self.assertEqual(actual, expected)
        
    def test_d_retirement_goal_met(self):
        actual = calculate_retirement(20, 100000, 15, 1000000)
        expected = [70, True]
        self.assertEqual(actual, expected)

    def test_e_retirement_goal_not_met(self):
        actual = calculate_retirement(50, 85000, 12.7, 1234567)
        expected = [135, False]
        self.assertEqual(actual, expected)

    def test_f_retirement_goal_not_met(self):
        actual = calculate_retirement(27, 65000, 7, 750000)
        expected = [150, False]
        self.assertEqual(actual, expected)

    def test_g_retirement_goal_not_met(self):
        actual = calculate_retirement(16, 23550, 15, 1500000)
        expected = [331, False]
        self.assertEqual(actual, expected)
