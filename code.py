room = "start"

key = 0

playing = True

print("You are inside a dark castle.")

print("There is a locked door in front of you.")

print("1. Go to the tower")

print("2. Go to the door")

choice = input("Choose 1 or 2: ")

if choice == "1":
    room = "tower"

if choice == "2":
    room = "door"

if room == "tower":

    print("You enter the tower.")

    print("You find a math puzzle.")

    print("What is 5 + 3 * 2?")

    print("a. 16")

    print("b. 11")

    print("c. 13")

    answer = input("Choose a, b or c: ")

    if answer == "b":

        print("Correct!")

        print("You found a key!")

        key = 1

    else:

        print("Wrong answer!")

if room == "door":

    if key == 1:

        print("You use the key.")

        print("The door opens!")

        print("You escaped the castle!")

    else:

        print("The door is locked.")

        print("You need a key.")