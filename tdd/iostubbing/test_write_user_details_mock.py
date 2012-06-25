import unittest
import write_user_details_di
import sys
import pymock

class TestUserDetails(pymock.PyMockTestCase):
    
    def test_output_file_contents(self):
        #mock the input proxy
        raw_input_provider = self.mock()
        mock_raw_input = raw_input_provider.raw_input
        self.expectAndReturn(mock_raw_input('What is your name ? '), 'Joe')
        self.expectAndReturn(mock_raw_input('What is your age ? '), '40')
        self.expectAndReturn(mock_raw_input('Which city do you stay in ? '), 'Pune')
        
        #mock the file handle
        mock_opener_interface = self.mock()
        mock_file = self.mock()
        self.expectAndReturn(mock_opener_interface.open('Joe.txt', 'w'), mock_file)
        mock_file.write('Name : Joe\n')
        mock_file.write('Age : 40\n')
        mock_file.write('City : Pune\n')
        mock_file.close()
        
        #replay
        self.replay()
        
        #call the actual method
        write_user_details_di.accept_and_write(iproxy=raw_input_provider.raw_input, opener=mock_opener_interface.open)
        
        #verify
        self.verify()
        
        
if __name__ == "__main__":
    unittest.main()