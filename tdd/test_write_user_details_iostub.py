import unittest
import write_user_details
import sys

def gen_open_stub(output_stub):
    def open(fpath, mode):
        return output_stub
    return open

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

class OutputStub(object):
    def __init__(self):
        self.values = []
        
    def write(self, value):
        self.values.append(value)
    
    def close(self):
        self.closed = True

        
class TestUserDetails(unittest.TestCase):
    
    def test_output_file_contents(self):
        values = ['Priyanka', '33', 'Mumbai']
        output_stub = OutputStub()
        write_user_details.open = gen_open_stub(output_stub)
        sys.stdin = InputStub(values)
        write_user_details.accept_and_write()
        name = output_stub.values[0]
        age = output_stub.values[1]
        city = output_stub.values[2]
        self.assertEqual(name[0:len(name)-1], 'Name : Priyanka')
        self.assertEqual(age[0:len(age)-1], 'Age : 33')
        self.assertEqual(city[0:len(city)-1], 'City : Mumbai')
        
if __name__ == "__main__":
    unittest.main()