import unittest
from bmi import calculate_bmi

class TestBMI(unittest.TestCase):           
    def test_a_bmi_and_category_underweight_correct(self):
        actual = calculate_bmi(5, 3, 100)
        expected = [18.1, "Underweight"]
        self.assertEqual(actual, expected)

    def test_b_bmi_and_category_normal_correct(self):
        actual = calculate_bmi(5, 3, 125)
        expected = [22.7, "Normal weight"]
        self.assertEqual(actual, expected)

    def test_c_bmi_and_category_overweight_correct(self):
        actual = calculate_bmi(5, 3, 150)
        expected = [27.2, "Overweight"]
        self.assertEqual(actual, expected)
        
    def test_d_bmi_and_category_obese_correct(self):
        actual = calculate_bmi(5, 3, 175)
        expected = [31.7, "Obese"]
        self.assertEqual(actual, expected)


