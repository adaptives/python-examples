#!/usr/bin/python

import os

def read_file(name):
  print 'printing contents of file ' + name
  f = None
  #We use try...finally to ensure that the file is closed even if there
  #is a problem while processing it
  try:
    f = file(name, 'r')
    line = f.readline()
    while(len(line) != 0):
      print line, #notice the , to prevent printing a newline character
      line = f.readline()
  finally:
    if f != None:
      f.close()

def create_module(name):
  print 'creating module ' + name
  f = None
  #We use try...finally to ensure that the file is closed even if there
  #is a problem while processing it
  try:
    f = file(name, 'w')
    #Notice that a newline is not inserted automatically
    #There is no println in Python
    f.write('#!/usr/bin/python\n')
    f.write('# Filename : ' + name + '\n')
    f.write("'''Class comment to be completed.'''\n")
    f.write('\n')
    f.write('def __init__():\n')
    f.write('\n')
    f.write('def __str__():\n')
    f.write('\n')
  finally:
    if f != None:
      f.close()

name = '/home/pshah/tmp/tmp.py'
#Use exceptions to make the program fail gracefully and provide a meaningful
#message to the user
try:
  create_module('/home/pshah/tmp1/tmp.py')
  read_file(name)
  #Remove the file so we do not pollute the disk
  os.remove(name)
except Exception, e:
  print 'An error ocurred in this program ', e
