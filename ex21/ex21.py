def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - % d" % (a, b)
    return a - b

def multiply(a, b):
    print"MULTIPLYING %d * % d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b


print "Let's do some math with functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d," % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That become: ", what, "Can you do it by hand?"

def formula(a, b, c, d, e):
    return a + (b - (c * (d / e)))

print formula(age, height, weight, iq, 2)

print "Simple formula: x ^2 + y/2 + 3"
x = 2
y = 12
print add(multiply(x, x), add(divide(y, 2), 3))