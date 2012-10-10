#extra credit challenge - 
#fit the entire copy script on a single line
#remove all the stupid prompts

from sys import argv
from os.path import exists

script, from_file, to_file = argv

#is it a problem if we never close the file later?
#you don't need to then do in_file.close() when you 
#reach the end of the script. It should already be closed by Python once that one line runs.
open(to_file, 'w').write(open(from_file).read())

