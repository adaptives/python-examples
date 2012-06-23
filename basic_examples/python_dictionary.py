#!/usr/bin/python

#A Python dictionary is a collection which contains key value pairs, where the
#key must be an immutable object

def print_dict(the_dict, msg="Contents of the dict"):
  print msg
  for key, value in the_dict.items():
    print key, value

pop = {'China' : 1337722000,
       'India' : 1162210000,
       'United States' : 306261000}

print 'The population of India is ', pop['India']

#We have 3 countried let's add 2 more
pop['Indonesia'] = 229976124
pop['Brazil'] = 191080000

print_dict(pop, 'The 5 highest populated countries in the world are (unsorted)')

#Let's say we decide to keep only top 3
del(pop['Indonesia'])
del(pop['Brazil'])

print_dict(pop, 'The 3 highest populated countries in the world are (unsorted)')

#This is how we define a class in Python
#This is a mutable class. We will see that it cannot be used as a key in a Python dict 
class SimpleMutableClass:
  def __init__(self, num):
    self.num = num

smc1 = SimpleMutableClass(4)
#maps can only have immutable objects as keys, we try putting a mutable object
illegal_dict = {smc1 : 4}
#We are able to create and print the map
print illegal_dict[smc1]
#Lets mutate the key
smc1.num = 6
#Mutation not reflected in the dict
assert illegal_dict[smc1] == 4
#But the change did happen
assert smc1.num == 6
