#!/usr/bin/python

class MyMethodNotImplementedError(Exception):
  def __init__(self):  
    Exception.__init__(self)

#We will raise an Error if this method is called. The purpose is to show which
#Error to use to signal that a method os not yet implemented and also to show
#how to raise Exceptions
def some_method():
  raise NotImplementedError

def another_method():
  raise MyMethodNotImplementedError()

try:
  some_method()
except NotImplementedError, e:
  print 'Method is not implemented ', e

another_method()
