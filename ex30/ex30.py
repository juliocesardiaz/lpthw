people = 30
cars = 25
trucks = 50


if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's just stay home then."

if (cars < people) & (trucks > people):
    print "Wow, when did we buy so many trucks."
else:
    print "Cool."