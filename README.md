Getting Started with Banking System with File System

A.
This code creates a basic banking system that stores data using the Python File System. 
Two test files (staff.txt and customer.txt) are included in this repo to run the codes
The staff.txt stores 2 staff details. The details include:
Username
Password
Email
Full Name

The customer.txt is empty

B.
On running the program, it presents the following options:

1 Staff Login
2 Close App

If the user selects Login, the user is asked for their username and password
The program checks the pre-defined staff in the staff.txt file and verify that the username and password are correct. 
If incorrect, user will see an error message and told to try again. 

C.
After user login is successful, a new file is created to store the user session.
After login, staff will be presented with the following options: 

1 Create new bank account
2 Check Account Details
3 Logout

D
If staff selects Create bank account, staff will supply the following information 

1 Account name
2 Opening Balance
3 Account Type
4 Account email

The details above will be saved in the customer.txt file and a 10 digits account number generated for the customer.
After the staff completes creating the account, the account number will be displayed, and then presented with the options in (C) above.

If Staff selects check account details from (C), the program should request for account number
The program should fetch the details of the account from the customer.txt file and display it to the staff, then present back the options in (C).

If staff selects logout in (C), the user session file and return the user back to the staff login page.

 

And finally, if staff selects Close App, the program should terminate.

 
