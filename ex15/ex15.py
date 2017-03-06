# imports the argv module from sys
from sys import argv

# unpacks argv into script and filename variables
script, filename = argv

# opens the file specified in argv as a file type 
txt = open(filename)

# prints out message to let you know it will print out the file
print "Here's your file %r: " % filename
print txt.read()

txt.close()