#Problem 6
#Find the difference between the sum of the squares of the 
#first one hundred natural numbers and the square of the sum.
#25164150

start_num = 1
end_num = 100
#make sure to include the last number of the range..
end_num += 1

def sum_of_squares(start, stop):
	sum = 0
	for x in range(start, stop):
		sum += x**2
	print sum
	return sum

def square_of_sum(start, stop):
	square = 0
	for y in range(start, stop):
		square += y
	print square
	return square ** 2 
	
print square_of_sum(start_num, end_num) - sum_of_squares(start_num, end_num)