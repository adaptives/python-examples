#!/usr/bin/python
# Filename : pythonic_objects

class Person:

  def __str__(self):
    the_str = ''
    if self.first_name != None:
      the_str += self.first_name
    if self.mi != None:
      the_str += self.mi
    if self.last_name != None:
      the_str += self.last_name
    return the_str 

  def __init__(self, **kwargs):
    self.first_name = None
    self.mi = None
    self.last_name = None
    if kwargs.has_key('first_name'):
      self.first_name = kwargs['first_name']
    if kwargs.has_key('mi'):
      self.mi = kwargs['mi']
    if kwargs.has_key('last_name'):
      self.last_name = kwargs['last_name']

person = Person(first_name='Larry', last_name='Wall')
print person
