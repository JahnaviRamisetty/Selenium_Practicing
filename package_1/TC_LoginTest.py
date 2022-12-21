import unittest

class LoginTest(unittest.TestCase):

    def test_LoginByEmail(self):
        print("this is the login test for email")
        self.assertTrue(True)

    def test_LoginByFacebook(self):
        print("This is the login by Facebook")
        self.assertTrue(True)

    def test_LoginByTwitter(self):
        print("This is the login by Twitter")
        self.assertTrue(True)


    if __name__ == '__main__':
        unittest.main()