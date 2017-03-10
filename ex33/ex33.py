def looper(x, increment):

    i = 0
    numbers = []

    while i < x:
        print "At the top i is %d" % i
        numbers.append(i)

        i += increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i


    print "The numbers: "

    for num in numbers:
        print num

def for_looper(x):
    numbers = range(x)

    print "The numbers: "
    for num in numbers:
        print num

looper(6, 1)
looper(3, 1)
looper(20, 2)
for_looper(6)