#!/usr/bin/python
# Filename : pythonic_objects.py

class Person:
  attr = ('first_name', 'mi', 'last_name')
  attr_defaults = {'first_name':None, 'mi':None, 'last_name':None}

  def __str__(self):
    return ' '.join(getattr(self, attr, ' ') for attr in Person.attr)

  def __init__(self, **kwargs):
    for attr in Person.attr:
      setattr(self, attr, kwargs.get(attr, Person.attr_defaults[attr]))

person = Person(first_name='Larry', last_name='Wall')
print person
