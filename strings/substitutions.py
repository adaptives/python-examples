#!/usr/bin/python
# Filename : substitutions.py
from string import Template

greeting = 'Hello'
name = 'John'

print("%s %s how are you?" %(greeting, name))

print "%(greeting)s %(name)s how are you?" % locals()

print Template('$greeting $name how are you?').substitute(locals())

#print("{greeting} {name} how are you?".format(**locals()))


print("My first program; {greeting}".format(**locals()))




