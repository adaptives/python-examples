import unittest

class TestUserDetails(unittest.TestCase):
    
    def setUp(self):
        super(TestUserDetails, self).setUp()
        
        
    def tearDown(self):
        super(TestUserDetails, self).tearDown()
        
        
    def test_output_file_contents(self):
        fp = open('Priyanka.txt')
        name = fp.readline()
        age = fp.readline()
        city = fp.readline()
        self.assertEqual(name[0:len(name)-1], 'Name : Priyanka')
        self.assertEqual(age[0:len(age)-1], 'Age : 33')
        self.assertEqual(city[0:len(city)-1], 'City : Mumbai')
        
if __name__ == "__main__":
    unittest.main()