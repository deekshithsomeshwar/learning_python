""" THis is a trial project to work as an atm"""

import getpass
import os

current_balance = 500
pin = 1234
cust_name = "Raja"
draw_limit = 1000
repeat = True


def main():
    count = 0
    pin = 1234
    while count <4:
        input=int(getpass.getpass('Enter pin: '))
        if input == pin:
            print("Access granted")
            break
        else:
            print("Access denied")
            count -=1

if __name__=='__main__':
    main()

def option():
    print ("1: withdraw cash, 2: deposit cash, 3: check balance, 4: quit")
    return input ("What would you like to do today?: ")
run = option()


while  True:
    while run == 1:
        amount = int(raw_input("How much would you like to withdraw: "))
        if amount <= current_balance:
            print ("Dispensing!! New balance is ${}" . format(current_balance - amount))
            current_balance=current_balance - amount
            break
        elif amount > current_balance:
            print ("Insufficient balance. Your current available balance is ${}". format(current_balance))
            break
    while run == 2:
        amount = int(raw_input("How much would you like to deposit: "))
        print("Update balance is ${}" .format(current_balance + amount))
        current_balance = current_balance + amount
        break
    while run == 3:
        print("Your current balance is ${}" .format(current_balance))
        break
    while run == 4:
        print("Closing!! Thank you")
        quit()
    if run > 4:
        print "Option not available!"
    optional = raw_input("Do you wish to continue? Y: yes, N: no: ")
    if optional == "N" or optional =="n":
        quit()
    elif optional== "Y" or optional== "y":
        run = option()
