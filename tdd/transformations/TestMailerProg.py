import unittest
import MailerProg
import os

class TestMailerProg(unittest.TestCase):

    def setUp(self):
        super(TestMailerProg, self).setUp()

    def tearDown(self):
        super(TestMailerProg, self).tearDown()

    def test_find_msg_files(self):
        fqn = os.path.abspath(__file__)
        msg_files = MailerProg.find_msg_files(fqn[0:fqn.rfind('/')])
        self.assertEqual(5, len(msg_files))
        self.assertTrue('email1.msg' in msg_files)
        self.assertTrue('email2.msg' in msg_files)
        self.assertTrue('email3.msg' in msg_files)
        self.assertTrue('email4.msg' in msg_files)
        self.assertTrue('email5.msg' in msg_files)

    def test_parse_msg_file(self):
        fqn = os.path.abspath(__file__)
        curr_dir = fqn[0:fqn.rfind('/')]
        msg = MailerProg.parse_msg_file(os.path.join(curr_dir,'email1.msg'))
        self.assertEqual(msg.to[0], 'user1@domaina.com')
        

if __name__ == "__main__":
    unittest.main()
