# https://realpython.com/pytest-python-testing/

# example of a test
def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"
    
    

# fixtures:
"""
pytest takes a different approach. It leads you toward explicit dependency declarations that are still reusable thanks to the availability of fixtures. 
pytest fixtures are functions that can create data, test doubles, or initialize system state for the test suite. 
Any test that wants to use a fixture must explicitly use this fixture function as an argument to the test function, 
so dependencies are always stated up front:
"""

import pytest

@pytest.fixture
def example_fixture():
    return 1

def test_with_fixture(example_fixture):
    assert example_fixture == 1



# conftest.py
"""
How to Use Fixtures at Scale

As you extract more fixtures from your tests, you might see that some fixtures could benefit from further abstraction. 
In pytest, fixtures are modular. Being modular means that fixtures can be imported, can import other modules, 
and they can depend on and import other fixtures. All this allows you to compose a suitable fixture abstraction for your use case.

For example, you may find that fixtures in two separate files, or modules, share a common dependency. In this case, 
you can move fixtures from test modules into more general fixture-related modules. That way, you can import them back into any test modules that need them. 
This is a good approach when you find yourself using a fixture repeatedly throughout your project.

If you want to make a fixture available for your whole project without having to import it, a special configuration module called conftest.py will 
allow you to do that.

pytest looks for a conftest.py module in each directory. If you add your general-purpose fixtures to the conftest.py module, then you’ll be able 
to use that fixture throughout the module’s parent directory and in any subdirectories without having to import it. This is a great place 
to put your most widely used fixtures.

Another interesting use case for fixtures and conftest.py is in guarding access to resources. Imagine that you’ve written a test suite for code 
that deals with API calls. You want to ensure that the test suite doesn’t make any real network calls even if someone accidentally writes a test 
that does so.
"""


# parametrise for slightly changing data
"""
Fixtures aren’t quite as useful when you have several tests with slightly different inputs and expected outputs. In these cases, 
you can parametrize a single test definition, and pytest will create variants of the test for you with the parameters you specify.
"""
@pytest.mark.parametrize("maybe_palindrome, expected_result", [
    ("", True),
    ("a", True),
    ("Bob", True),
    ("Never odd or even", True),
    ("Do geese see God?", True),
    ("abc", False),
    ("abab", False),
])
def test_is_palindrome(maybe_palindrome, expected_result):
    assert is_palindrome(maybe_palindrome) == expected_result
