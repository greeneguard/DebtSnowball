import os
import sys
import math
#import table
import datetime
from operator import itemgetter, attrgetter

os.system('cls')

#account object has name, amount, apr, and minimium payment
class Account:
    def __init__(self, name, amt, apr, minPay, t):
        self.name = name
        self.amount = float(amt)
        self.apr = float(apr/12)
        self.miniPay = float(minPay)
        self.debt = t
        self.totalPayment = 0
        self.totalInterest = 0
        if t == True:
            self.balance = float(amt)
        elif t == False:
            self.balance = 0

    #representation of object
    def __repr__(self):
        return '\n Name:{} APR:{:2.2%} Balance:${:,.2f}'.format(self.name, self.apr*12, self.balance)
           
    def payment_schedule(self,e):
        global extra
        self.payment = self.miniPay + e

        #calculate payment, principle and balance for debt
        if self.debt == True:
            self.interest = self.apr * self.balance
            #adjust payment if payment is greater than remaining balance
            if self.balance + self.interest <= self.payment:
                self.payment = self.balance + self.interest
            self.principle = self.payment - self.interest
            self.balance = self.balance - self.principle
            
        #calcualte payment, balance and principle of savings    
        elif self.debt == False:
            self.interest = self.apr * (self.amount - self.balance)
            #adjust payment if payment is greater than remaining balance
            if self.amount + self.balance <= self.payment:
                self.payment = self.amount - self.balance
            self.principle = self.payment + self.interest
            self.balance = self.balance + self.principle

        #print out current payments, interest, and balance for current account in month
        #print(
            #' Account:', self.name,
            #' Payment:', "$%.2f" % self.payment,
            #' Interest:', "$%.2f" % self.interest,
            #' Balance:', "$%.2f" % self.balance
            #)

        #print out the total for payment and interest for this account.
        self.totalPayment = self.totalPayment + self.payment
        self.totalInterest = self.totalInterest + self.interest

#assign accounts
walmart = Account("Walmart", 1033, .244, 39, True)
amazon = Account("Amazon", 1330, .25, 30, True)
AES6 = Account('AES 6', 4111, .0535, 38, True)
allyBank = Account('Ally Bank', 13947.56, .1631, 300, True)
carSavings1 = Account('Malibu Replacement', 10000, .02, 0, False)
carSavings2 = Account('Escape Replacement', 10000, .02, 0, False)
houseDownPayment = Account('House Downpayment', 20000, .002, 0, False)
GL721 = Account('Great Lakes 721', 3443.62, .045, 30, True)
GL722 = Account('Great Lakes 722', 6082.75, .0655, 47, True)
GL723 = Account('Great Lakes 723', 6536.27, .0655, 51, True)
GL724 = Account('Great Lakes 724', 8220.42, .0535, 37, True)
AES9 = Account('American Education Services 9', 6887.03, .0425, 59, True)
GL725 = Account('Great Lakes 725', 13565.97, .0655, 75, True)
emergencyLiving = Account('Emergency Living', 20874.88, .02, 0, False)
emergencyfund = Account('Emergency Fund', 1000, .02, 0, False)

#create list of accounts
global accountsList
accountsList = [amazon, walmart, allyBank, GL721, GL722, GL723, GL724, AES9, GL725, emergencyfund]

#sort list smallest to largest
accountsList = sorted(accountsList, key = attrgetter('amount'), reverse=False)
print(accountsList)

def add_account(self):
    global accountsList
    if self.name == "Emergency Fund":
        accountsList.append(emergencyLiving)
    elif self.name == "Ally Bank":
        accountsList.append(carSavings1)
    elif self.name == "Malibu Replacement":
        accountsList.append(carSavings2)
    elif self.name == "Escape Replacement":
        accountsList.append(houseDownPayment)
    elif self.name == "House Downpayment":
        mortgage = Account('Mortgage', ((houseDownPayment.balance / .1)- houseDownPayment.balance), .08, 1000, True)
        accountsList.append(mortgage)

    #print("Congradulations! ", self.name, "has been paid off!")
    print(self.name, "$%.2f" % self.totalPayment, "$%.2f" % self.totalInterest, math.floor(m/12), "years", m % 12, "months")
    global extra
    extra = extra + self.miniPay
    accountsList.remove(self)
    accountsList = sorted(accountsList, key = attrgetter('amount'), reverse=False)
    #print(accountsList)
    #print()
    
def remove_account(a):
    if a.debt == True:
        if a.balance <= 0:
            add_account(a)
            
    if a.debt == False:
        if a.balance >= a.amount:
            add_account(a)
            
#initialize monthly counter varaible
global m
m = 1

#set global extra payment, default 50
global extra
try:
    extra = float(input('Enter amount for extra payment:  '))
except:
    extra = 50

#Visual check the number of accounts in accountsList
#print(len(accountsList))

#as long as an account has a balance loop through paymaent cycles
print()
while len(accountsList) > 0:
    #print out the current month
    #print('month', m)
    #print(extra)

    for i in range(len(accountsList)):
        #assign standing variable to current account. see line 30
        try:
            if i == 0:
                accountsList[i].payment_schedule(extra)
            else:
                accountsList[i].payment_schedule(0) 

        except:
            print('Error')
            break
            sys.exit()

    #iterate monthly counter
    m = m+1
    #create a seperate function to delete the account once finished.
    remove_account(accountsList[0])

sys.exit()
#End Program
