import AddressBook
import os
import copy
import validate
import Entrant

'''
AddressBook Manager
Michael Barnett, 2019

main.py handles basic UI, input validation and address book loading.
AddressBook.py contains main addressbook class and handles related functions.
Entrant.py contains entrant class.
'''

addressBooks = []
test = AddressBook.Address()
addressBooks.append(test)
currentSelected = addressBooks[0]

# ---------- Begin UI functions ----------
# Functions run when user selects an option in the menu. related to name.
def newCustomer():
    first = input("\nPlease enter the new customers first name: ")
    last = input("Please enter the new customers last name: ")
    phone = input("Please enter the new customers phone number: ")
    if (currentSelected.createEntrant(first, last, phone) == 1):
        print("Customer added successfully!")
    else:
        print("Error!")
    input("Press enter to return.")

def removeCustomer():
    remID = input("\nPlease enter the customer ID of the deletee: ")
    if(currentSelected.removeEntrant(remID) == 1):
        print("Customer removed successfully!")
    else:
        print("Cannot find customer ID!")
    input("Press enter to return.")

def addAddressBook():
    addName = validate.validateText("\nPlease enter the new address books name: ", ['\\', '/', ':', '?', '"', '<', '>', '|'], None)
    i = AddressBook.Address()
    i.bookName = addName
    addressBooks.append(i)
    print("Added {0}!".format(addName))
    input("Press enter to return.")

def changeAddressBook():
    global currentSelected
    addName = input("\nPlease enter the address book you would like to read: ")
    for i in addressBooks:
        if (i.bookName == addName):
            # Prevent potential variable reference instead of value issues
            currentSelected = None
            currentSelected = i

def printCustomer(entrantList,bookname):
    if (len(entrantList) == 0):
        print("No entries in this address book!")
    else:
        results = copy.deepcopy(entrantList)
        for i in results:
            i.entrantID = "({0}) {1}".format(bookname, i.entrantID)
        currentSelected.printEntrant(results)
    input("Press enter to return.")

def searchCustomer():
    global currentSelected
    print("\nWhich address book(s) would you like to search?")
    print("1. All address books")
    for y in range(0, len(addressBooks)):
        print("{0}. {1}".format(y+2, addressBooks[y].bookName))
    bookSelect = validate.validateInt("Enter the associated number: ", None)
    print("\nWhich field would you like to search?")
    print("1. First Name")
    print("2. Last Name")
    print("3. Phone Number")
    searchField = validate.validateInt("Enter the associated number: ", None)
    searchTerm = input("\nEnter the search term: ")
    currentSelected.printEntrant(searchInBook(searchTerm, bookSelect, searchField))
    input("\nPress enter to return.")

# ---------- Start menu handling functions ----------
# Functions responsible for keeping a consistant UI experience

def searchInBook(term, book, field):
    returnList = []
    if (book == 1):
        for x in addressBooks:
            entrants = x.searchEntrant(field, term)
            for i in entrants:
                # Prepare data for display in UI
                i.entrantID = "({0}) {1}".format(x.bookName, i.entrantID)
                for j in returnList:
                    if (checkForDupes(i,j)):
                        j.entrantID += ", {0}".format(i.entrantID)
                        entrants.remove(i)
            returnList.extend(entrants)
    else:
        results = addressBooks[book-2].searchEntrant(field, term)
        for i in results:
            # Prepare data for display in UI
            i.entrantID = "({0}) {1}".format(addressBooks[book-2].bookName, i.entrantID)
        returnList.extend(results)
    print("\nWe found the following entrants;")
    return returnList

def checkForDupes(ent1, ent2):
    if (type(ent1) not in [Entrant.Entrant]):
        raise TypeError("ent1 is not an Entrant!")
    if (type(ent2) not in [Entrant.Entrant]):
        raise TypeError("ent2 is not an Entrant!")

    # Check if each value of both entrants are the same (IDs are always different)
    if (ent1.firstName.lower() == ent2.firstName.lower()):
        if (ent1.lastName.lower() == ent2.lastName.lower()):
            if (ent1.phoneNumber.lower() == ent2.phoneNumber.lower()):
                return True
    return False

def inputHandle(value):
    if (value == 1):
        newCustomer()
    elif (value == 2):
        removeCustomer()
    elif (value == 3):
        printCustomer(currentSelected.bookEntries,currentSelected.bookName)
    elif (value == 4):
        searchCustomer()
    elif (value == 5):
        changeAddressBook()
    elif (value == 6):
        addAddressBook()

def mainloop():
    exit = False
    while (exit == False):
        print("\n"*10)
        print("~~ AddressBook Manager ~~")
        print("Current Address Book: {0}\n".format(currentSelected.bookName))
        print("What would you like to do?")
        print("1. Create a new customer")
        print("2. Remove a customer")
        print("3. Print customer details")
        print("4. Search for customers")
        print("5. Change Address Book")
        print("6. Create a new Address Book")
        value = validate.validateInt("Enter the associated number: ", None)
        inputHandle(value) 

# ---------- Begin loading functions ----------

def loadAddressBook():
    global addressBooks
    global currentSelected
    for root, dirs, files in os.walk("./books/"):
        for name in files:
            newBook = AddressBook.Address()
            newBook.loadFromDisk(os.path.join(root, name))
            addressBooks.append(newBook)
            currentSelected = newBook

if __name__ == "__main__":
    loadAddressBook()
    mainloop()