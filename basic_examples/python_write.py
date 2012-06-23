# from sys module import a member called 'argv'
from sys import argv
#unpack
script, filename = argv
fp = open(filename, "w")
print "Writing to file %r " % fp
fp.write("Hello World")
fp.close()
