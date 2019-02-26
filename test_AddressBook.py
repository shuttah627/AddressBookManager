import unittest
from AddressBook import Address

class TestAddressBook(unittest.TestCase):

    def test_createEntrant_types(self):
        self.assertRaises(TypeError, Address.createEntrant, (True, True, True))
        self.assertRaises(TypeError, Address.createEntrant, (1,2,3))

    def test_removeEntrant_types(self):
        self.assertRaises(TypeError, Address.removeEntrant, (self, 222))
    
    def test_searchEntrant_types(self):
        self.assertRaises(TypeError, Address.searchEntrant, (self, "test", "test"))

    def test_searchEntrant_values(self):
        self.assertRaises(ValueError, Address.searchEntrant, self, 50, "test")
        self.assertRaises(ValueError, Address.searchEntrant, self, -1, "test")

    def test_printEntrant_types(self):
        self.assertRaises(TypeError, Address.printEntrant, (self, "Hello!"))
        self.assertRaises(TypeError, Address.printEntrant, (self, 22))
        self.assertRaises(TypeError, Address.printEntrant, (self, True))
        self.assertRaises(TypeError, Address.printEntrant, (self, {}))

    def test_loadFromDisk_types(self):
        self.assertRaises(TypeError, Address.loadFromDisk, (None))
        self.assertRaises(TypeError, Address.loadFromDisk, (True))
        self.assertRaises(TypeError, Address.loadFromDisk, (1234))
        self.assertRaises(TypeError, Address.loadFromDisk, ({}))
        self.assertRaises(TypeError, Address.loadFromDisk, ([]))

    def test_loadFromDisk_values(self):
        self.assertEqual(Address.loadFromDisk(self, '?'), 0)