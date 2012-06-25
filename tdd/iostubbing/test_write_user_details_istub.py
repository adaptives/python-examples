import unittest
import write_user_details
import sys

class InputStub(object):
    def __init__(self, values):
        self.values = values
        self.cnt = 0
        
    def readline(self):
        if self.cnt < len(self.values):
            ret_val = self.values[self.cnt]
            self.cnt += 1 
            return ret_val        
        else:
            raise StopError()
    
class TestUserDetails(unittest.TestCase):
    
    def test_output_file_contents(self):
        values = ['Priyanka', '33', 'Mumbai']
        sys.stdin = InputStub(values)
        write_user_details.accept_and_write()
        fp = open('Priyanka.txt')
        name = fp.readline()
        age = fp.readline()        
        city = fp.readline()
        self.assertEqual(name[0:len(name)-1], 'Name : Priyanka')
        self.assertEqual(age[0:len(age)-1], 'Age : 33')
        self.assertEqual(city[0:len(city)-1], 'City : Mumbai')
        
if __name__ == "__main__":
    unittest.main()