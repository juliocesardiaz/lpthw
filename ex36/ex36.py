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
    print "Sphinx: \'Hello, answer this riddle and I will let you pass, otherwise I will devour you whole.\'"
    print "Sphinx: \'What walks on four legs in the morning three in the afternoon and two at night?\'"

    answer = raw_input('> ')
    if answer.lower == "man":
        print "Sphinx: \'You are correct, enter this room."
        room_e()
    else:
        dead("The sphinx devoured you're head.")

def room_c():
    print "You enter a room with three levers. Which one do you pull?"

    lever = raw_input('> ')
    if lever == "2":
        print "You pull down the second lever. A door opens, and you go through it."
        room_f()
    elif lever == "1":
        dead("As you pull the first lever a green gass enters the room. You suffocate.")
    elif lever == "3":
        dead("You pull down the thrid lever, darkness opens up below your feet and you are enveloped in it.")
    else:
        print "That is not a lever, try again! Hint: Choose a lever by inputting 1-3."

def room_d():
    dead("You enter the room, instantly your heart is removed from your body.")

def room_e():
    print "There are two doors in front of you choose one."

    choice = raw_input('> ')
    if choice == "1":
        room_c()
    elif choice == "2":
        room_i()
    else:
        print "That's not a door, try again! Hint: Choose a door by inputting 1-3."

def room_f():
    