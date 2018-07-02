import random

def main():
    print "Guess a number between 1 and 100"
    randomNumber = random.randint(1,100)
    found = False #flag variable to see if they guessed it

    while not found:
        userGuess = int(raw_input("Your guess: "))
        if userGuess == randomNumber:
            print "you got it"
            found = True
        elif userGuess > randomNumber:
            print "Guess lower"
        else:
            print "Guess higher"
if __name__=='__main__':
    main()
