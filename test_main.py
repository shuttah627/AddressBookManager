import unittest
import main
import Entrant
import copy

class TestMain(unittest.TestCase):
    def test_checkForDupes_values(self):
        en1 = Entrant.Entrant("","","")
        en2 = en1
        self.assertTrue(main.checkForDupes(en1, en2))

        en2 = copy.deepcopy(en1)
        en2.firstName = "Test"
        self.assertFalse(main.checkForDupes(en1,en2))

    def test_checkForDupes_types(self):
        self.assertRaises(TypeError, main.checkForDupes, ("Hello", "There!"))