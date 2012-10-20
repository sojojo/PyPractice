#Problem 4
#Find the largest palindrome made from the product of two 3-digit numbers.

largest = 0
for x in range(100, 999):
	for y in range(100, 999):
		product = x * y
		product_length = len(str(product))
		split_place = 10 ** (product_length // 2)
		#even number of digits
		if product_length % 2 == 0:
			if product // split_place == product % split_place:
				largest = product
		else:
			if product // (split_place * 10) == product % split_place:
				largest = product
print largest