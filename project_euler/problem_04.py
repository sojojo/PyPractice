#Problem 4
#Find the largest palindrome made from the product of two 3-digit numbers.
#906609

low_range = 100
high_range = 999

largest_x = 0
largest_y = 0
largest = 0
for x in range(low_range, high_range):
	for y in range(low_range, high_range):
		product = x * y
		product_length = len(str(product))
		#find which decimal place we should split at
		split_place = 10 ** (product_length // 2)
		#even number of digits
		if product_length % 2 == 0:
			if product // split_place == int(str(product % split_place)[::-1]):
				if largest < product:
					largest = product
					largest_x = x
		else:
			#need to shift where the split occurs if its odd
			if product // (split_place * 10) == int(str(product % split_place)[::-1]):
				if largest < product:
					largest = product
					largest_y = y

print """
The number %d and %d make a product that is the biggest palindrome
that uses numbers < %d.
""" % (largest_x, largest_y, high_range)
print largest
