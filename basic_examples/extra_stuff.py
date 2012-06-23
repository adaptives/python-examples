#!/usr/bin/python

import os

#If there is only one statement that would have gone in the block then it can
#be specified in the same line
if os.name == 'posix': print 'You are cool'

def say_hello(): return 'hello'
print say_hello()

#List comprehensions
class Employee:

  def __str__(self):
    return self.name + ' ' + str(self.salary)
  
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary
  

employees = []
employees.append(Employee('Tom', 30000))
employees.append(Employee('Satish', 40000))
employees.append(Employee('Harry', 50000))

#Let's get a list of all employees whose salaries are greater than 30000
#using list comprehensions
sal_more_than_40k = [e for e in employees if e.salary > 40000] 
print 'Listing ' + str(len(sal_more_than_40k)) + ' employees with sal > 40k'
for emp in sal_more_than_40k: 
  print emp

#Now let's get something similar using lambda expressions
sal_more_than_30k = filter(lambda e : e.salary > 30000, employees)
print "Listing " + str(len(sal_more_than_30k)) + " employees with sal > 30k"
for emp in sal_more_than_30k:
  print emp

#`` and repr return a canonical form of an object in the form if a string
#We can control what repr returns with the __repr__() method
print repr(sal_more_than_30k)
print `sal_more_than_30k`
eval(repr(sal_more_than_30k))
