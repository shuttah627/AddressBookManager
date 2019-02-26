import validate
import Entrant
import unittest

class TestValidation(unittest.TestCase):
    

    def test_validateInt_values_true(self):
        self.assertAlmostEqual(validate.validateInt("Int Test 1: ",1), 1)
        self.assertAlmostEqual(validate.validateInt("Int Test 2: ", 9999999999999999999),9999999999999999999)

    def test_validateText_values_true(self):
        self.assertEqual(validate.validateText("Text Test 1: ",['?'],"hello!"),"hello!")

    def test_validateText_values_false(self):
        self.assertNotEqual(validate.validateText("Text Test 2: ",['?'],"hello!"),"Hello!")
        