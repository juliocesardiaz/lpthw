print "Hello, pick a number between 1-4."

choice = raw_input("> ")

if choice == "1":
    print "Ha you lose."
elif choice == "2":
    print "Interesting choice."
elif choice == "3":
    print "You have won."
elif choice == "4":
    print "Terrible trerible choice."
else:
    print "Good, I didn't want to play either."