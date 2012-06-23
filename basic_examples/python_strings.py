#!/usr/bin/python

#Note: Python strings are immutable

#Strings can be enclosed in single quotes
print 'Hello World in single quotes'

#Strings can also be enclosed in double quotes
print "Hello World in double quotes"

#Strings can also be enclosed in triple quotes
print """ This is a multiline string
Such strings are also possible in Groovy.
These strings can contain ' as well as " quotes """

#Strings can be continued on the next line
print "This string is continued on the\
next line (in the source) but a newline is not added"

#Raw strings
print r"The newline character is represented with \n"

#The following is a unicode string, but here it is a literal. 
#How do we specify that a string read from a file should be held 
#as a unicode string. Also the +uXXXX notation does not work in
#Python
print u"This is a unicode string u0600"

#See how the strings are concatenated
print 'hello ' 'world'

#Notice how the print statement accepts , separated values
print '2 + 3 = ', (2+3)

#Getting the length of a string
greeting = "Hello my dear friend how are you?"
print "the length of string '" ,greeting, "' is ", len(greeting)

#Let's check if the string contains the word 'Hello'
if('Hello' in greeting):
  print 'This greeting seems to be in English'

if(greeting.find('Hello') != -1):
  print 'This greeting seems to be in English'
