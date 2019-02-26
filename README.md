# AddressBookManager
Python 3.6 implementation of an cli based (technically) Address Book Manager

## Features
This project includes the following features;
- Adding full names and phone numbers into your address book
- Removing existing contact entries
- Printing all contacts in an address book
- Managing and switching between multiple address books
- Searching and printing results accross singular and multiple address books, without doubled up entries.
- A simple implementation of "In Memory Persistance" (data is held in RAM, only saves to file when anything changes, seamless saving experience).

This project includes a very rudimentary user interface, mainly for function testing, and demo use. I would highly recommend 'playing around' with the program.

## Unit Tests
The project also includes unit tests for all major validation and address book functions.
For said unit tests, this project uses Python 3.6's standard unittest library.
In order to run these tests, call `python -m unittest` on your CLI in the repo's root folder.
You can read the tests yourself in the `test_*.py` files.

## Ideas for future expansion
- Encrypt the address book data on disk
- Build a proper user interface with PyQt or Tkinter
- or separate the UI functions out of main.py
- Implement OS specific features (clear screen for example)
