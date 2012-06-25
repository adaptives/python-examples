import unittest
import test_write_user_details
import test_write_user_details_istub

suite1 = unittest.TestLoader().loadTestsFromTestCase(test_write_user_details.TestUserDetails)
suite1.addTests(unittest.TestLoader().loadTestsFromTestCase(test_write_user_details_istub.TestUserDetails))

unittest.TextTestRunner(verbosity=2).run(suite1)