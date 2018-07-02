stock = {"apples":5, "oranges":2, "pears":0}
alreadyAte = []

def menu():
    print ("Press 1: to add stock")
    print ("Press 2: to check stock")
    print ("Press 3: to enter a purchase")
    print ("Press 4: to quit the program")
    return input("What would you like to do: ")

run = menu()

while True:
    if run == 1:
        addStock = raw_input('Food to be added to stock?: ')
        amount = int(input('quantity of food to be added to stock: '))
        stock[addStock] = amount
        run = menu()
    elif run == 2:
        for key, value in stock.items():
            print ("{}: {}" . format(key,value))
        run = menu()
    elif run == 3:
        food = raw_input("What food was eaten: ")
        person = raw_input("who ate the food: ")
        if food in stock:
            if person in alreadyAte:
                print ("{} was sent to the brig" .format(person))
                run = menu()
            else:
                if stock[food] > 0:
                    stock[food] -= 1
                    alreadyAte.append(person)
                    print alreadyAte
                    print ("{} ate {}" .format(person, food))
                    run = menu()
                else:
                    print ("{} didnt eat as we are out of {}" . format(person, food))
                    run = menu()
        else:
            print ("{} are out of stock" . format(food))
            run = menu()
    elif run == 4:
        break

print ("The program has ended")
