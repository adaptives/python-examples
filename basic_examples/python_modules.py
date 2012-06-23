#!/usr/bin/python

import sys
import my_module

#printing all the command line arguments provided to this program
print "cmd args to this program are '", sys.argv, "'"

print 'The PYTHONPATH is ', sys.path 

#Let's call a function from my_module
my_module.sayHello()
