print "You enter a dark room with three doors. Do you go through door #1, door #2 or door #3?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear
elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"
elif door == "3":
    print "You enter a room, with an enterance to a cave and a door. Which do you go through?"
    print "1. Cave."
    print "2. Door."

    enterance = raw_input("> ")

    if enterance == "1":
        print "You have entered the cave, it is covered in gold and jewels, in the corner you see a lever."
        print "1. Take gold."
        print "2. Pull lever"

        gold = raw_input("> ")

        if gold == "1":
            print "As you stuff gold into your pockets, the enterance shuts and the room is filled with sand. You suffocate beneath the layers of sand."
        elif gold == "2":
            print "You pull the lever, a hole opens up beneath your feet. You drop 200 feet to your death."
        else:
            print "You sit down and dream about the past."
    elif enterance == "2":
        print "You open the door  behind is a T-rex, he eats you in one bite."
    else:
        print "Good choice, just go home."
else:
    print "You stumble around and fall on a knife and die. Good job!"