#using a few pointers from: http://www.daniweb.com/software-development/python/code/216880/check-if-a-number-is-a-prime-number-python
#Find the sum of all the primes below two million.

def prime_number(max_num):
	total = 0
	#find each prime number until we hit num_primes 
	for i in range(0, max_num):
		#start testing primes from the last prime number we found
		
		prime = True
		#iterate through all smaller numbers and test whether its prime
		if i < 2:
			prime = False
		elif i == 2:
			prime = True
		elif i % 2 == 0:
			prime = False
		else:
			for j in range(2, i / 2):
				if i % j == 0:
					prime = False
		if prime == True:
			total += i
			print i, total
			
		#print total
	return total
	
print prime_number(2000000)