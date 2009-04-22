#!/usr/bin/python
# Filename : python_files.py
import os

def read_file(name):
  print 'printing contents of file ' + name
  f = file(name, 'r')
  line = f.readline()
  while(len(line) != 0):
    print line, #notice the , to prevent printing a newline character
    line = f.readline()
  f.close()

def create_module(name):
  print 'creating module ' + name
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
  f.close()

name = '/home/pshah/tmp/tmp.py'
create_module(name)
read_file(name)
#Remove the file so we do not pollute the disk
os.remove(name)
