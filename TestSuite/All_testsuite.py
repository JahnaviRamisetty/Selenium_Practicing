import unittest

from package_1.TC_LoginTest import LoginTest
from package_1.TC_Signup import signuptest
from package2.TC_payment import paymentTest

tc0 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc1 =unittest.TestLoader().loadTestsFromTestCase(signuptest)
tc2=unittest.TestLoader().loadTestsFromTestCase(paymentTest)

sanityTestSuite=unittest.TestSuite([tc0,tc1])
functionalTestSuite=unittest.TestSuite([tc2])
masterTestSuite=unittest.TestSuite([tc0,tc1,tc2])

unittest.TextTestRunner(verbosity=2).run(masterTestSuite)




