#Problem 1
#http://projecteuler.net/problem=1
#Find the sum of all the multiples of 3 or 5 below 1000.

highest_number = 1000
multiple1 = 3
multiple2 = 5

sum = 0
i = 0
while i < highest_number:
	if i % multiple1 == 0 or i % multiple2 == 0:
		sum += i
	i += 1
		
print sum