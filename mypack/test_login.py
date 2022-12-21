import pytest


@pytest.yield_fixture()
def setup():
    print("opening the url")
    yield
    print("closing the url")


def test_loginbyfacebook(setup):
    print("login by facebook")

def test_loginbyemail(setup):
    print("login by email")

