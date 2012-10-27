#Problem 7
#What is the 10 001st prime number?
#..assuming that we don't know what the prime numbers are, beforehand
#104743
#brute force - this has very bad efficiency. 
#It'd be better to eliminate multiples of numbers to a certain point.

def prime_number(num_primes):
	latest_prime = 1
	#find each prime number until num_primes have been found
	for i in range(0, num_primes):
		#start testing primes from the last prime number we found
		num_pointer = latest_prime + 1
		
		prime = False
		#increase the count until we find the next prime
		while prime == False:
			prime = True
			#iterate through all smaller numbers and test whether its prime
			for j in range(2, num_pointer):
				if num_pointer % j == 0:
					prime = False
			num_pointer += 1
		latest_prime = num_pointer - 1
		#print latest_prime
	return latest_prime
	
print prime_number(10001)