#Project Euler - Problem 19
#http://projecteuler.net/problem=19
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

starting_year = 1900
ending_year = 2000

#months
year_calendar = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_year_calendar = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#1 Jan 1900 was a Monday.
current_year = starting_year
current_calendar = year_calendar
current_day = 0

sundays_on_1st = 0

while current_year < ending_year:
	#is this a leap year?
	#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400
	if (current_year - starting_year) % 4 != 100 or (current_year - starting_year) % 4 == 0:
		current_calendar = leap_year_calendar
	for c in current_calendar:
		#if it is sunday and it is the first of the month
		if (current_day) % 7 == 6: 
			sundays_on_1st += 1
		#set current_day to next 1st of the month
		current_day += c
	current_year += 1
	
print """
There are %d Sundays that fall on the 1st between 1900 and 2000""" % sundays_on_1st