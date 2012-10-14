#Exercise 20: Functions And Files
from sys import argv

script, input_file = argv

#print the contents of the file
def print_all(f):
	print f.read()
	
#put the pointer back at the front of the file
def rewind(f):
	f.seek(0)

#print a number and whichever line the pointer is on.	
def print_a_line(line_count, f):
	print line_count, f.readline()
	
current_file = open(input_file)

print "Let's print the whole file"

print_all(current_file)

print "Now let's rewind, kind of like a tape"

rewind(current_file)

print "Let's print three lines:"

current_line = 1 
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)