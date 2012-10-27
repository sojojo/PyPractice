#Problem 9 
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
#31875000 with a = 200, b = 375, c = 475

sum = 1000

#screw it. I'm using brute force. No side can be negative, therefore the largest side possible is equal to the sum
for a in range(0, sum):
	for b in range(0, sum):
		for c in range (0, sum):
			if (a ** 2 + b ** 2 == c ** 2) and (a + b + c == sum) and a < b and b < c:
				print a, b, c
				print a * b * c