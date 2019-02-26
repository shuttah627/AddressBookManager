import Entrant
import random
import string
import json
import copy

class Address():

    bookName = ""
    bookEntries = []

    def __init__(self):
        self.bookEntries = []
        self.bookName = "New Book"

    def saveToDisk(self):
        # json in Python gives easy methods for converting objects into a string of json, and back.
        jsonObj = { "bookName": self.bookName, "entrants": [] }
        for i in self.bookEntries:
            entrantObj = { "entrantID": i.entrantID, "firstName": i.firstName, "lastName": i.lastName, "phoneNumber": i.phoneNumber }
            jsonObj["entrants"].append(entrantObj)
        try:
            with open("./books/"+self.bookName+".adbk", 'w') as f:
                f.write(json.dumps(jsonObj))
                return 1
        except:
            print("Failed to save addressbook to disk.")
            return 0

    def loadFromDisk(self, filename):
        if (type(filename) not in [str]):
            raise TypeError("filename needs to be a string!")
        
        loadedJSON = ""
        try:
            with open(filename, 'r') as f:
                loadedJSON = json.loads(f.read())
        except:
            print("Cannot find address book of filename {0}".format(filename))
            return 0
        # Function only called on construction of books from disk. setting self.bookName is required.
        self.bookName = loadedJSON["bookName"]
        for i in loadedJSON["entrants"]:
            loadedEntrant = Entrant.Entrant(i['firstName'], i['lastName'], i['phoneNumber'])
            loadedEntrant.entrantID = i["entrantID"]
            self.bookEntries.append(loadedEntrant)
        return 1
    
    def generateRandomID(self):
        unique = False
        while (unique == False):
            # create an array of random chars, then join them with an empty delimiter. combines array together into string.
            newID = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=5))
            for i in self.bookEntries:
                if (getattr(i, 'entrantID') == newID):
                    unique = False
                else:
                    unique = True
            if (len(self.bookEntries) == 0):
                unique = True
        return newID

    def createEntrant(self, firstname, lastname, phone):
        if (type(firstname) not in [str]):
            raise TypeError("firstname must be a string!")
        if (type(lastname) not in [str]):
            raise TypeError("lastname must be a string!")
        if (type(phone) not in [int,str]):
            raise TypeError("phone must be an int or string!")

        i = Entrant.Entrant(firstname, lastname, phone)
        i.entrantID = self.generateRandomID()
        self.bookEntries.append(i)
        self.saveToDisk()
        return 1
    
    def removeEntrant(self, remID):
        if type(remID) not in [str]:
            raise TypeError("removeEntrant only accepts strings!")

        for i in range(0, len(self.bookEntries)):
            if (getattr(self.bookEntries[i], "entrantID") == remID):
                self.bookEntries.remove(self.bookEntries[i])
                self.saveToDisk()
                return 1
        return 0

    def searchEntrant(self, field, term):
        if type(field) not in [int]:
            raise TypeError("field only accepts an int!")
        if (field > 3 or field <= 0):
            raise ValueError("The desired search field doesnt exist!")

        returnList = []
        fieldToSearch = ""
        if (field == 1):
            fieldToSearch = "firstName"
        elif (field == 2):
            fieldToSearch = "lastName"
        elif (field == 3):
            fieldToSearch = "phoneNumber"

        for i in range(0, len(self.bookEntries)):
            if term.lower() in getattr(self.bookEntries[i], fieldToSearch).lower():
                returnList.append(self.bookEntries[i])
        # Python loves passing by reference (the append statement above), and passing by value is required here.
        return copy.deepcopy(returnList)

        
    def printEntrant(self,entrantlist):
        if type(entrantlist) not in [list]:
            raise TypeError("Entrant list must be a list!")

        for i in range(0, len(entrantlist)):
            print("~~~~~~~~~~~\nCustomer {0} of {1}".format(i+1,len(entrantlist)))
            print("Book and ID: {0}".format(getattr(entrantlist[i], 'entrantID')))
            print("First Name: {0}".format(getattr(entrantlist[i], 'firstName')))
            print("Last Name: {0}".format(getattr(entrantlist[i], 'lastName')))
            print("Phone Number: {0}".format(getattr(entrantlist[i], 'phoneNumber')))

