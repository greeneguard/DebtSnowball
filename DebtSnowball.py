
import os
import math
import amortization
#import table
import datetime
from operator import itemgetter, attrgetter

os.system('cls')

#account object has name, amount, apr, and minimium payment
class account:
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

    def stepOne(self):
        global extra
        if self.balance > 0:
            #adjust payment if current account is the lowest balance. see line 49
            if i == 0:
                self.paymentSchedule(extra)
            else:
                self.paymentSchedule(0)
        #remove current account from list
        else:
            extra = extra + self.miniPay
            print(
                self.name,
                'Total Payment:', "$%.2f" % self.totalPayment,
                'Total Interest:', "$%.2f" % self.totalInterest,
                '\n')
            accountsList.remove(self)
            print(accountsList)
            
    def paymentSchedule(self,e):
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
walmart = account("Walmart", 1033,.244, 39, True)
amazon = account("Amazon", 1330, .25, 30, True)
AES6 = account('AES 6', 4111, .0535, 38, True)
allyBank = account('Ally Bank', 13947.56, .1631, 300, True)
carSavings1 = account('Malibu Replacement', 10000, .002, 0, False)
carSavings2 = account('Escape Replacement', 10000, .002, 0, False)
houseDownPayment = account('House Downpayment', 20000, .002, 0, False)
mort = account('Mortgage', 200000, .8, 0, True)


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


    accountsList = sorted(accountsList, key = attrgetter('amount'), reverse=False)
    
    #print out the current month
    print('month', m)

    for i in range(len(accountsList)):
        #assign standing variable to current account. see line 30
        accountsList[i].stepOne()

        #check triggers for savings
        #when car loan is paid off start savings for Malibu replacement
        if allyBank not in accountsList and carSavings1 not in accountsList:
            accountsList.append(carSavings1)
        #when first care is saved up for start saving for second
        if carSavings1 not in accountsList and carSavings2 not in accountsList:
            accountsList.append(carSavings2)
        #when second car is saved up for start saving for down payment
        if carSavings2 not in accountsList and houseDownPayment not in accountsList:
            accountsList.append(houseDownPayment)
        #when down payment is saved up start paying off mortgage
        if len(accountsList) == 1 and mortgage not in accountsList:
            accountsList.append(mortgage)
            
    #iterate monthly counter
    m = m + 1
    if len(accountsList) == 0:
        break
#End Program
