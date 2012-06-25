"""
In this file we accept some details from the user and write them
to a file. 
"""
        
def accept_and_write():
    name = raw_input('What is your name ? ')
    age = raw_input('What is your age ? ')
    city = raw_input('Which city do you stay in ? ')
    
    fp = open(name+'.txt', 'w')
    fp.write("Name : %s\n" % name)
    fp.write("Age : %s\n" % age)
    fp.write("City : %s\n" % city)
    fp.close()
    
if __name__ == "__main__":
    accept_and_write()
    