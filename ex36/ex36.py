from sys import exit

def enterance():
    print "You have entered a dungeon, beginning your adventure."
    print "It is said that within this dungeon a great trasure lies."
    print "Be careful though as there are many traps and puzzles along the way."
    print "Before you are three doors. Which do you choose to go through?"

   while True: 
        choice = raw_input('> ')

        if choice == "1":
            room_b()
        elif choice == "2":
            room_c()
        elif choice == "3":
            room_d()
        else:
            print "That's not a room, try again! Hint: Choose a room by inputting 1-3."

def room_b():
    print "You enter a room, in it you find a Sphinx."
    print "Sphinx: \'Hello, answer this riddle and I will let you choose a door, otherwise I will devour you whole.\'"
    print "Sphinx: \'What walks on four legs in the morning three in the afternoon and two at night?\'"

    answer = raw_input('> ')
    if answer.lower == "man":
        print "Sphinx: \'You are correct, choose one of the two doors."

        choice = raw_input('> ')
        if choice == "1":
            room_c()
        elif choice == "2":
            room_i()
        else:
            print "That's not a room, try again! Hint: Choose a room by inputting 1 or 2."
    else:
        dead("The sphinx devoured you're head.")
def room_c():
    