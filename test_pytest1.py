import pytest
@pytest.yield_fixture()
def setup():
    print("execute one before the test method")
    yield
    print("after the test method")

def testmethod1(setup):
    print("this is test method1")

def testmethod2(setup):
    print("this is test method2")



