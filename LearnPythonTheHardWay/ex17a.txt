#script to copy one file to another
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#note that there's only 1 parameter for reading
in_file = open(from_file)
indata = in_file.read()

print "The input is %d bytes long" % len(indata)

print "Does the file exist? %r" % exists(to_file)

print "Ready. Hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done"

out_file.close()
in_file.close()