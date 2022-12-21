import unittest

class signuptest(unittest.TestCase):
    def test_signupemail(self):
        print("this is sign up by email")
        self.assertTrue(True)

    def test_signupfacebook(self):
        print("this is sign up by facebook")
        self.assertTrue(True)
if __name__== "__main__":
    unittest.main()
