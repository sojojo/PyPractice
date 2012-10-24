#Problem 5
#What is the smallest positive number that is evenly divisible 
#by all of the numbers from 1 to 20
#232792560

low_num = 1
high_num = 20
smallest_divisor = 0
count = high_num

while smallest_divisor == 0:
	num_divisible = 0
	for x in range(low_num, high_num):
		if count % x == 0:
			num_divisible += 1
	if num_divisible == high_num - low_num:
		smallest_divisor = count
	#count more quickly - increment by the largest number
	count += high_num
print smallest_divisor