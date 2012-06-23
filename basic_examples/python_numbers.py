#!/usr/bin/python

print "8 is an integer ", 8

num = 8
print "8 is an integer and 'num' is a variable referring to an integer", num

print "8/4 is 2. let's check ", num/4
print "But why is 8/3 also 2 ? ", num/3
print """
Maybe because when integers are divided, the result is also an integer.
Which means the result is truncated. Maybe if we used floats we might get
a better answer.
"""

num = 8.0
print "8.0/3.0 = ", num/3.0

print """
ok great. BTW I hope you realized how we were able to assign 'num' to a float
after assigning it to an int. This is because Python is not a statically 
typed language. We could have assigned 'num' to a String as well.
"""

#What is the default type of numbers in Python... compare this with Groovy
max64BitInt = 2**64 - 1
bigNum = max64BitInt + 126
print 'This is a big number ', bigNum

#Python has the floor dividion operator as well as the power operator
#I do not think Java has any of these. Groovy probably has the power op
print '4//3 = ', 4//3

#See the GroovyNumbers program and verify that all concepts appear here as well
