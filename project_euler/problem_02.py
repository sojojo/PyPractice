#Problem 2
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
#answer = 4613733

limit = 4000000

n = 1
m = 2
total = n

while m < limit:
	if m % 2 == 0:
		total += m
	t = n + m
	n = m
	m = t

print total