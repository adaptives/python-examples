#!/usr/bin/python
# Filename : using_modules.py
import sys
import my_module

#printing all the command line arguments provided to this program
print 'sys.path = ', sys.argv

print 'The PYTHONPATH is ', sys.path 

my_module.sayHello()
