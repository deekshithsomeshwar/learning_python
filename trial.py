""" THis is a trial project to work as an atm"""

import getpass

current_balance = 1000
pin = 1234
cust_name = "Raja"
draw_limit = 1000
success = False

i = 0
l = 3

def main():
    print ("1: withdraw cash, 2: deposit cash, 3: check balance, 4: quit")
    choice = raw_input("What would you like to do today?: ")
    input = int(getpass.getpass("Enter your pin number: "))


run = main()

while input == pin:
    if choice == 1:
        while True:
            amount = int(raw_input("How much would you like to withdraw: "))
            if amount <= 1000:
                print ("Dispensing!! New balance is ${}" . format(current_balance - amount))
            elif amount > 1000:
                print ("Amount cannot exceed 1000")
            elif amount > current_balance:
                print ("Insufficient balance. Your current available balance is ${}". format(current_balance))
                print ("")
    elif run == 2:
        while True:
            amount = int(raw_input("How much would you like to deposit: "))
            print("Update balance is ${}" .format(current_balance + amount))

    elif run == 3:
        print("Your current balance is ${}" .format(current_balance))

    elif run == 4:
        print("Thank you")

    else:
        break
while input != pin:
     input = int(getpass.getpass("Enter your pin number again: "))
     run = main()
