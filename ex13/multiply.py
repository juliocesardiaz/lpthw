from sys import argv

script, x = argv
z = int(x)
y = int(raw_input("Enter a second number to get multiplied: "))
print "%d times %d equals %d" % (z, y, (z * y))