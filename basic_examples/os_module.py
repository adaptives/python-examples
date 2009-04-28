#!/usr/bin/python
# Filename : sys_module.py

#The os module exposes various operating system related details and
#functionality. In this module we will explore some of the more commonly
#needed functionality

import os

print 'Your operating system: ', os.name
print 'Your login name: ', os.getlogin()
print 'Your current working directory is: ', os.getcwd()
print 'Your system path is: ', os.getenv('PATH')
