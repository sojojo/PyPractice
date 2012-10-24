#Project - example 36
#make a text based adventure similar to example 35
#it's supposed to be a general solution, but it hasn't turned out too well yet

from sys import exit

#each scene that the character goes through is formatted the same way
def new_area(title, message, actions):
	print "\n~~~~%s~~~~\n" % title
	print message
	while True:
		take_action(actions)
		next = raw_input("> ")
		if next == "?":
			print "\n--Help--\n"
			print "General directions:"
			print "\t? - \thelp\n\texit - \texits program\n"
		elif next == "exit":
			exit(0)
		else:
			i = 0
			for n in actions:
				if next == n:
					return i
				i += 1
			print "Bad input. Try again\n"

	
def take_action(actions):
	message = "Valid actions: "
	for n in actions:
		message += n + ", "
	message += "or ? for help"
	print message

cave_title = "Trogdor the Cave wanderer"
cave_text = "You enter a dank cave. Darkened marks are left on the wall from massive fires from long ago. There is a sturdy wooden door ahead, a dark passage with smoke coming from it to the right, and a pool of spring water to the left. \nWhich direction will you go?\n"
cave_actions = ['left', 'right', 'front', 'back']
cave_move = new_area(cave_title, cave_text, cave_actions)
if cave_move == 0:
	print "burned alive!"
elif cave_move == 1:
	print "drowned!"
elif cave_move == 2:
	print "stubbed toe!"
else:
	print "wimp"

"""
elif next == 'forward':
	print "You inspect the wooden door, but it won't budge without a key."
	print "The text on the door warns that a terrible ogre is there"

"""