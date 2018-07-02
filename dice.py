# dice game by Deekshith Someshwar

import random
numbersPlayed1 = []
numbersPlayed2 = []
numbersplayed3 = []
users = []

def game():

    print ("1: Play, 2: View previoys roll, 3: Close game , 4: Change player")
    return input ("What would you like to do? ")

print ("This is a 3 player dice game. Please enter your names \n")

player1 = raw_input("Enter 1st player name: ")
while not player1:
    player1 = raw_input("Cant be empyt. Enter 1st player name: ")
users.append(player1)

player2 =  raw_input("Enter 2nd player name: ")
while not player2:
    player2 =  raw_input("Cant be empyt. Enter 2nd player name: ")
while player2 == player1:
    player2 =  raw_input("Cant be the same as other players. Enter 2nd player name: ")
users.append(player2)

player3= raw_input("Enter 3rd player name: ")
while not player3:
    player3 =  raw_input("Cant be empyt. Enter 3rd player name: ")
while player3 == player1 or player3 == player2:
    player3 =  raw_input("Cant be the same as other players. Enter 2nd player name: ")
users.append(player3)

print ("Welcome {}" .format(users))
trial = raw_input("Who is playing? :")

run = game()
while True:
    if run == 1:
        dice = (1,8)
        roll = random.randint(1,8)
        print roll
        run = game()
        if trial == player1:
            numbersPlayed1.append(roll)
        elif trial == player2:
            numbersPlayed2.append(roll)
        elif trial == player3:
            numbersplayed3.append(roll)
        else:
            print("user not available")
            break
    elif run == 2:
        if trial == player1:
            print numbersPlayed1
        elif trial == player2:
            print numbersPlayed2
        elif trial == player3:
            print numbersplayed3
        run = game()
    elif run == 3:
        break
    elif run ==4:

        print ("The game has ended")
    print numbersPlayed1
    print numbersPlayed2
    print numbersplayed3
