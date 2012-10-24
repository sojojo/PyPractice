#Excersise 33: While Loops
#while loop intro

#EC make a function
def num_list(n, increment):
	i = 0 
	numbers = []

	while i < n:
		print "At the top i is %d" % i
		numbers.append(i)
		
		i = i + increment
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
		
	print "The numbers: "

	for num in numbers:
		print num
		
num_list(20, 5)
