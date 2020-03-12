
import os
import math
import amortization
#import table
import datetime
from operator import itemgetter, attrgetter

#def extra to be payed monthly

#account object has name, amount, apr, and minimium payment
class account:
    def __init__(self, name, amt, apr, minPay, t):
        self.name = name
        self.amount = float(amt)
        self.apr = float(apr/12)
        self.miniPay = float(minPay)
        self.debt = t
        self.balance = float(amt)
        self.totalPayment = 0
        self.totalInterest = 0

    #representation of object
    def __repr__(self):
        return '\n Name:{} APR:{:2.2%} Balance:${:,}'.format(self.name, self.apr*12, self.balance)


    def paymentSchedule(self,e):
        self.interest = self.apr * self.balance
        self.payment = self.miniPay + e

        #adjust payment if payment is greater than remaining balance
        if self.balance + self.interest <= self.payment:
            self.payment = self.balance + self.interest

        #calculate the principle and balance after payment
        self.principle = self.payment - self.interest
        self.balance = self.balance - self.principle
        
        #print out current payments, interest, and balance for current account in month
        print(
            ' Account:', self.name,
            ' Payment:', "$%,.2f" % self.payment,
            ' Interest:', "$%,.2f" % self.interest,
            ' Balance:', "$%,.2f" % self.balance
            )

        #print out the total for payment and interest for this account.
        self.totalPayment = self.totalPayment + self.payment
        self.totalInterest = self.totalInterest + self.interest
        
        #Print out total payments and interest and delete account if balance is paid off
        if self.balance <= 0:
            extra = extra + self.miniPay
            print(
                self.name,
                'Total Payment:', "$%,.2f" % self.totalPayment,
                'Total Interest:', "$%,.2f" % self.totalInterest
                )

#assign accounts
walmart = account("Walmart", 1033,.244, 39, True)
amazon = account("Amazon", 1330, .25, 30, True)
student_loan1 = account('SL1', 3443.62, .0425, 29.05, True)
student_loan2 = account('SL2', 6082.75, .0655, 46.97, True)


#create list of accounts
accountsList = [amazon, walmart, student_loan1, student_loan2]

#sort list smallest to largest
accountsList = sorted(accountsList, key = attrgetter('amount'), reverse=False)
print(accountsList)

#initialize monthly counter varaible
m = 1

#set extra payment, default 50
exta = input('Enter amount for extra payment' or 50)

#Visual check the number of accounts in accountsList
print(len(accountsList))

#as long as an account has a balance loop through paymaent cycles
while len(accountsList) > 0:
    #print out the current month
    print('month', m)
    
    #
    for i in range(len(accountsList)):
        #assign standing variable to current account
        acct = accountsList[i]
        try:
            #Visual check account itereator and balance
            #print(i)
            #print(acct.balance)
            #if the balance of the current account is greater than 0, run payment schedule
            if acct.balance > 0:
                #adjust payment if current account is the lowest balance
                if i == 0:
                    acct.paymentSchedule(extra)
                else:
                    acct.paymentSchedule(0)
            #remove current account from list
            else:
                accountsList.remove(acct)
                print(accountsList)
                break
            #iterate monthly counter
            m = m + 1

        except:
            i = 0
            print(accountsList)
            break
    break
#End Program
