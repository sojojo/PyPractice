#RegEx Practice
#http://docs.python.org/howto/regex.html
import re

pattern1 = r'[1990-2100]'
file_name = 'sample_twitter.txt'

file = open(file_name)
line = "Hello 2012 you are 1999"
line = file.read()

matchObj = re.search( '\d\d\d\d', line, re.M|re.I)
#find strings that look like years
all_years = re.findall( '20[01]\d', line)

if matchObj:
   print "matchObj.group() : ", matchObj.group()
   print "matchObj.start() : ", matchObj.start()
   print "matchObj.end() : ", matchObj.end()
   print "matchObj.span() : ", matchObj.span()
else:
   print "No match!!"

if all_years:
	for a in all_years:
		print a

#print line
#match_obj = re.match(pattern2, file, re.M|re.I)
#print match_obj.group()