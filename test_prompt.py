import unittest
from prompt import user_prompt

class TestValidPromptInput(unittest.TestCase):
    def test_a_exit_choice_success(self):
        with self.assertRaises(SystemExit) as cm:
            user_prompt("x")
        self.assertEqual(cm.exception.code, 0)
            
    def test_b_bmi_choice_success(self):
        actual = user_prompt("1")
        expected = ["1", True]
        self.assertEqual(actual, expected)

    def test_c_bmi_choice_fail(self):
        actual = user_prompt(1)
        expected = [1, False]
        self.assertEqual(actual, expected)      

    def test_d_retirement_choice_success(self):
        actual = user_prompt("2")
        expected = ["2", True]
        self.assertEqual(actual, expected)

    def test_e_retirement_choice_fail(self):
        actual = user_prompt(2)
        expected = [2, False]
        self.assertEqual(actual, expected)

    def test_f_invalid_input(self):
        actual = user_prompt("this is not valid input")
        expected = ["this is not valid input", False]
        self.assertEqual(actual, expected)
        
