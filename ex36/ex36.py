from sys import exit

def enterance():
    print "You have entered a dungeon, beginning your adventure."
    print "It is said that within this dungeon a great treasure lies."
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
    if answer == "man":
        print "Sphinx: \'You are correct, enter this room."
        room_e()
    else:
        dead("Your answer was wrong. The sphinx devoured you're head.")

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
    print "You enter the room, there is a huge dragon and a sheild on the floor and a sword on the other side."
    print "What do you do?"
    print "1. Grab sheild and sheild yourself?"
    print "2. Go for sword?"
    print "3. Sit in a ball and cry."

    choice = raw_input('> ')
    if choice == "1":
        dead("As you go for the sheild, the dragon shoots fire and turns you into ash instantly.")
    elif choice == "2":
        dead("As you go for the sword the dragon slashes you with its huge claws and you bleed out.")
    elif choice == "3":
        print "The Dragon feel sorry for you and let's you pass to the next room."
        room_g()
    else:
        dead("I don't know what that does but the dragon kills you instantly.")

def room_g():
    print "There is a computer, on it you see the following math problem."
    print "Solve for x: x^2 - 4 = 5"

    answer = raw_input('> ')
    if answer.isdigit():
        x = int(answer)
    else:
        dead("Learn how to type a number, you die instantly.")
    
    if x == 3:
        print "Well done, that is the correct answer. The door to the next room opens and you go through it."
        room_h()
    else:
        dead("Wrong answer, brush up on your algebra. The computer desintegrates your atoms.")

def room_h():
    print "Hooray you won the game."
    print "The room is full of treasure, you use it to become king and rule the land."
    print "Congratulations!"
    exit(0)

def room_i():
    print "You enter a room and there is a portal and a door, which do you take?"
    print "1. Portal."
    print "2. Door."

    while True:

        choice = raw_input('> ')
        if choice == "1":
            print "You enter the portal, it transports you back in time to the beginning."
            enterance()
        elif choice == "2":
            room_h()
        else:
            print "That is not a choice, try again! Hint: Choose by inputting 1 or 2."

def dead(cause):
    print cause, "Game Over"
    exit(0)

enterance()