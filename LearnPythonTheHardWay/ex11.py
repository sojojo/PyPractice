#more info on raw_input: http://docs.python.org/library/functions.html#raw_input

print "How old are you?"
age = raw_input('--> ')
print "How tall are you?",
height = raw_input()
print "How much do you weigh?", 
weight = raw_input()

print "So you're %r old, %r tall and %r heavy" % (age, height, weight)