"""
In this file we accept some details from the user and write them
to a file. 
"""

class InputProxy():
    def raw_input(self, msg):
        return raw_input(msg)


def accept_and_write(iproxy=raw_input, opener=open):
    name = iproxy('What is your name ? ')
    age = iproxy('What is your age ? ')
    city = iproxy('Which city do you stay in ? ')
    
    fp = opener(name+'.txt', 'w')
    fp.write("Name : %s\n" % name)
    fp.write("Age : %s\n" % age)
    fp.write("City : %s\n" % city)
    fp.close()