#TECH6301 Project: Bank Account
#UWO Continuing Studies
#RoboGarden
#Developed in IDLE SHELL 3.11.5
#October 2023

import math
from random import randint

def main():

    #~~~~~Steps 1 -> 3
    class BankAccount:

        #Constructor
        def __init__(self, name, accountType, balance=0):

            self.name = name
            self.accountType = accountType
            self.balance = balance

            #---Generate 8-Digit ID for the new account
            self.accountNumber = 0 
            for n in range(8):
                #ID is 8 randomly generated digits (1,...,8,9) concated together
                self.accountNumber += int(randint(1,9)*math.pow(10,n))


            #---Create a new file for each new account

            #Assign filename in accordance to the specified format
            self.filename = str(self.accountNumber) + "_" + self.accountType + "_" + self.name + ".txt"
            
            #Create a new file - append mode to maintain order
            self.accountStatement = open(self.filename, "a+")

            #Setup and Format file
            self.accountStatement.write("~~~~~~~~~~~~~~~~~~~~~\n ACCOUNT INFORMATION \n~~~~~~~~~~~~~~~~~~~~~\n")
            self.accountStatement.write("\n>>Account Holder: " + self.name)
            self.accountStatement.write("\n>>Account ID Number: " + str(self.accountNumber))
            self.accountStatement.write("\n>>Account Type: " + self.accountType)
            self.accountStatement.write("\n\n~~~~~~~~~~~~~~~~~~~~~\n Transaction History \n~~~~~~~~~~~~~~~~~~~~~\n")

            #Initial Transaction 
            self.accountStatement.write("\nDeposit: +$" + str(self.balance))
            self.accountStatement.write("\nBalance: $" + str(self.balance))
            self.accountStatement.write("\n---------")
            
            return

        #~~~~~Step 4 - Deposit Money
        def deposit(self, m_in):
            self.balance += m_in

            #---Append Transaction to Statement File
            self.accountStatement = open(self.filename, "a+")
            self.accountStatement.write("\nDeposit: +$" + str(m_in))
            self.accountStatement.write("\nBalance: $" + str(self.balance))
            self.accountStatement.write("\n---------")
            self.accountStatement.close()
            

        #~~~~~Step 5 - Withdraw Money
        def withdraw(self, m_out):
            #Ensure that withdrawal amount is less than the account balance
            if m_out <= self.balance:
                self.balance -= m_out
                #---Append Transaction to Statement File
                self.accountStatement = open(self.filename, "a+")
                self.accountStatement.write("\nWithdraw: -$" + str(m_out))
                self.accountStatement.write("\nBalance: $" + str(self.balance))
                self.accountStatement.write("\n---------")
                self.accountStatement.close()
            else:
                print("ID: " + str(self.accountNumber) + " - NAME: " + self.name + " - Overdraft Attempted. No Money Withdrawn.")
                self.accountStatement = open(self.filename, "a+")
                self.accountStatement.write("\nInvalid withdrawal attempted")
                self.accountStatement.write("\nBalance: $" + str(self.balance))
                self.accountStatement.write("\n---------")
                self.accountStatement.close()


        #~~~~~Step 6 - Get Account Balanace
        def get_balance(self):
            #print("Balance: $" + str(self.balance) + "\n")
            return self.balance

        #~~~~~Step 7
        #User ID
        def get_id(self):
            #print("Account ID Number: " + str(self.accountNumber) + "\n")
            return self.accountNumber

        #Username
        def get_name(self):
            #print("Account Holder: " + self.name + "\n")
            return self.name

        #Account Type
        def get_type(self):
            #print("Account Type: " + self.accountType + "\n")
            return self.accountType

        #~~~~~Step 8
        #Transaction History from statement file
        def get_transactions(self):

            #Transaction history starts from 13th line or 12th index of the statement file
            statement_file = open(self.filename, "r")
            statement_read = statement_file.readlines()
            history = statement_read[12:] #only capture the lines of concern
            statement_file.close()
            print("\n\n===>Transaction History ~ ID: " + str(self.accountNumber) + " - NAME: " + self.name + "\n")
            for action in history:
                print(action)
            print("\n===>End Of Transaction History\n")

    #====================================
    #----------------TEST----------------
    #====================================


    """
    Test 1
    -Deposit and withdraw within balance limits
    -Get name, ID, account type, and balance
    """
    t1 = BankAccount("Sarah", "Checking", 100000)
    t1.deposit(23456)
    t1.withdraw(56)
    #Username
    print("Account Holder: " + t1.get_name() + "\n")
    #Account ID
    print("Account ID Number: " + str(t1.get_id()) + "\n")
    #Account Type
    print("Account Type: " + t1.get_type() + "\n")
    #Account Balance
    print("Balance: $" + str(t1.get_balance()) + "\n")

    """
    Test 2
    -Perform several deposits
    """
    t2 = BankAccount("Mary", "Checking")
    t2.deposit(50)
    t2.deposit(50)
    t2.deposit(50)
    t2.deposit(50)
    t2.deposit(90000)

    """
    Test 3
    -Attempt to withdraw amounts greater than balance -> not allowed
    """
    t3 = BankAccount("Harvey", "Savings", 100)
    t3.deposit(100)
    t3.withdraw(2000)
    t3.withdraw(20000)
    t3.deposit(20)
    t3.withdraw(200)

    """
    Test 4
    -Get transaction history from statement file
    -Withdraw full balance
    """
    t4 = BankAccount("Gretel", "Savings", 500)
    t4.deposit(500)
    t4.deposit(1000)
    t4.withdraw(1234)
    t4.deposit(1500)
    t4.deposit(3000)
    t4.withdraw(t4.get_balance()) #Withdraw full balance
    t4.deposit(1)
    t4.deposit(9999999)
    t4.get_transactions() #Transaction History

    print("\n\n~*~*~*~*~Tests Completed. Thank You.")

main()
        

        
