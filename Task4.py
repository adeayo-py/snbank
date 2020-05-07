"""
A simple Bank simulation
"""
import re
from random import randint
import os

def welcome():
    print('Welcome to startNG bank')
    userprompt=input('Type 1 to login or 2 To close session\n>>')
    return userprompt

#create class for bank operations
class Bank:
    file = open('file.txt')

    def __init__(self):
        self.fhandle = open('customer.txt', 'r+')

    #method to validate staff password and usermane from staff file
    def validateUser(self,password,username):

        for line in Bank.file:
            line=line.rstrip()
            #Using regex for validation
            if re.search(username,line) and (re.findall(".*\['(\S+?)'",line) ==[password]):
                print('Successful login')
                print()
                Bank.file.close()
                return True
        else:
            print('Account details not found')
            Bank.file.close()
            return False

    #method to create account from user details
    def createAccount(self,name,balance,type,email):
        #Generate account number
        account=randint(1000000000,9999999999)
        print()
        print('Your account number is',account)
        print()
        #Save this into file
        self.fhandle.write(f'Hello {name} your {type} account number is {account} and your balance is {balance} Naira')
        self.fhandle.write('\n')
        self.fhandle.close()
        print('Account successfully created')

    #Method to display account details from customer file
    def displayAccount(self,accnum):
        self.fhandle = open('customer.txt', 'r+')
        for line in self.fhandle:
            if re.search(str(accnum), line):
                return line
        else:
            return 'Account number not found'

    def closeApp(self):
        print('Closing...\nThank you')
        quit()


#class for staff operations
class Staff:
    #Creating session file
    sessionfile = open('sessionfile.txt', 'w')

    #Collect username and password from staff for validation
    def login(self):
        self.username = input('Kindly enter your username: ')
        self.password=input('Kindly enter your password: ')
        return self.password,self.username

    #Create new account; prompting user for account name, type, email address and opening balance
    def newAccount(self):
        self.accName=input('Type account name: ')
        while True:
            #Block and character aside integer
            try:
                self.openBalance=int(input('Input your opening balance: '))
                break
            except:
                print('Invalid input')

        self.accType=input('Kindly select account type.\nS for Savings and C for current account\n>> ')
        #Make sure there are only two options S and C
        while True:
            if self.accType.upper()=='S':
                self.accType='Savings'
                break
            elif self.accType.upper()=='C':
                self.accType='Current'
                break
            else:
                print('Invalid input')
                self.accType = input('Kindly select account type.\nS for Savings and C for current account\n>> ')

        self.emailAdd=input('Input your email address: ')
        #Adding details to session file
        Staff.sessionfile.write(f'Staff creating account\nName: {self.accName}\nBalance: {self.openBalance} '
                                f'Account type: {self.accType}\nEmail address: {self.emailAdd}\n')


        return self.accName, self.openBalance,self.accType,self.emailAdd

    #Request account details from customer file
    def requestAccount(self):

        while True:
            # Block and character aside integer
            try:
                self.accnum=int(input('Type your ten digits account number: '))
                break
            except:
                print('Invalid input')

        Staff.sessionfile.write(f'Staff provides {self.accnum} to check account details')
        return self.accnum

#creating objects for Bank and Staff class
bank=Bank()
staff=Staff()


userprompt=welcome()
while True:
    if userprompt=='1':
        password,user=staff.login()
        valid=bank.validateUser(password,user)

        if valid:

            while True:
                validQuestions = input('Select 1 to create new bank account, 2 to Check Account Details, 3 to logout\n>> ')
                if validQuestions=='1':

                    name,balance,type,email=staff.newAccount()
                    bank.createAccount(name,balance,type,email)

                elif validQuestions=='2':
                    accountNumber=staff.requestAccount()
                    print(bank.displayAccount(accountNumber))

                elif validQuestions=='3':
                    #Closing session file and deleting
                    Staff.sessionfile.close()
                    os.remove('sessionfile.txt')
                    Bank.file = open('file.txt')
                    userprompt=welcome()

                    break
        else:
            print('Incorrect login details')
            Bank.file = open('file.txt')
            userprompt = input('Type 1 to login or 2 To close session\n>>')

    elif userprompt=='2':
        bank.closeApp()

    else:
        print('Type either 1 or 2')
        userprompt = input('Type 1 to login or 2 To close session\n>>')
