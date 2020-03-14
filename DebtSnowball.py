
import os
import sys
import math
import amortization
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

    def step_one(self):
        global extra

        #adjust payment if current account is the lowest balance. see line 49
        if i == 0:
            self.payment_schedule(extra)
        else:
            self.payment_schedule(0)

    #remove current account from list
    def remove_account(self):
        global extra
        if self.balance == self.amount or self.balance <= 0:
            extra = extra + self.miniPay
            print(
                self.name,
                'Total Payment:', "$%.2f" % self.totalPayment,
                'Total Interest:', "$%.2f" % self.totalInterest,
                '\n')
            if self.name == 'Ally Bank':
                accountsList.append(carSavings1)
            elif self.name == "Malibu Replacement":
                accountsList.append(carSavings2)
            elif self.name == "Escape Replacement":
                accountsList.append(HouseDownPayment)
            elif self.name == "House Downpayment":
                accountsList.append(mortgage)
                
            accountsList.remove(self)
            print(accountsList)
            accountsList = sorted(accountsList, key = attrgetter('amount'), reverse=False)
            
    def payment_schedule(self,e):
        global extra
        global accountsList
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
            if self.balance + self.interest <= self.payment:
                self.payment = self.balance + self.interest
            self.principle = self.payment + self.interest
            self.balance = self.balance + self.principle

        #print out current payments, interest, and balance for current account in month
        print(
            ' Account:', self.name,
            ' Payment:', "$%.2f" % self.payment,
            ' Interest:', "$%.2f" % self.interest,
            ' Balance:', "$%.2f" % self.balance
            )

        #print out the total for payment and interest for this account.
        self.totalPayment = self.totalPayment + self.payment
        self.totalInterest = self.totalInterest + self.interest


#assign accounts
walmart = Account("Walmart", 1033,.244, 39, True)
amazon = Account("Amazon", 1330, .25, 30, True)
AES6 = Account('AES 6', 4111, .0535, 38, True)
allyBank = Account('Ally Bank', 13947.56, .1631, 300, True)
carSavings1 = Account('Malibu Replacement', 10000, .02, 0, False)
carSavings2 = Account('Escape Replacement', 10000, .02, 0, False)
houseDownPayment = Account('House Downpayment', 20000, .002, 0, False)
mort = Account('Mortgage', 200000, .8, 0, True)


#create list of accounts
accountsList = [amazon, walmart, allyBank]

#sort list smallest to largest
accountsList = sorted(accountsList, key = attrgetter('amount'), reverse=False)
print(accountsList)

#initialize monthly counter varaible
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
while len(accountsList) > 0:
    #print out the current month
    print('month', m)

    for i in range(len(accountsList)):
        #assign standing variable to current account. see line 30
        try:
            accountsList[i].step_one()

            #iterate monthly counter
            m = m + 1
        except:
            print('Error')
            print(i)
            print(accountsList[i])
            i = i - 1
            sys.exit()
            
    #create a seperate function to delete the account once finished.
    accountsList[0].remove_account()
    
#End Program
