import unittest

class paymentTest(unittest.TestCase):
    def test_paymentindollars(self):
        print("payment in dollars")
        self.assertTrue(True)

    def test_paymentinrupees(self):
        print("payment in rupees")
        self.assertTrue(True)

if __name__=="__main__":
    unittest.main()