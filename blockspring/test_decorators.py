import pytest
import blockspring

# ***** Fixtures ****** #

def decorator_fixture(a,b=0):
    """This will be the test function for our decorator"""
    return a+b

def block_fixture(request, response):
    mySum = request.params["num1"] + request.params["num2"]
    response.addOutput('sum', mySum)
    response.end()

@pytest.fixture
def request():
    request = blockspring.Request()
    return request

@pytest.fixture
def response():
    response = blockspring.Response()
    return response

@pytest.fixture
def wrapped():
    wrapped = blockspring.decorate(decorator_fixture)
    return wrapped

########## Tests #########

def test_decorator_respects_name(wrapped):
    assert wrapped.__name__ == 'decorator_fixture'

def test_creates_blockspring_function(wrapped,request, response):
    assert response.result['_blockspring_spec']==True
    

def test_adds_output(wrapped, request, response):

    request.addHeaders({'b':1, 'c':3}) #<--this doesn't work
    test = wrapped(request, response)
    assert response.response['output']==4
    pass

