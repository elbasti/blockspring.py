import pytest
import blockspring

# ***** Fixtures ****** #

def decorator_fixture(a,b=0):
    """This will be the test function for our decorator"""
    return a+b

def dict_outputs(a, b):
    """returns a dict"""
    output = {}
    return {'a_squared':a*a, 'b_squared':b*b}

def list_outputs(a, b):
    """returns a list"""
    return [a*a, b*b]

@pytest.fixture
def request():
    request = blockspring.parse({'a':1, 'b':3})
    return request

@pytest.fixture
def response():
    response = blockspring.Response()
    return response

@pytest.fixture
def wrapped():
    wrapped = blockspring.decorate(decorator_fixture)
    return wrapped

@pytest.fixture
def dict_output_wrapped():
    wrapped = blockspring.decorate(dict_outputs)
    return wrapped

@pytest.fixture
def list_output_wrapped():
    wrapped = blockspring.decorate(list_outputs)
    return wrapped

########## Tests #########

def test_decorator_respects_name(wrapped):
    assert wrapped.__name__ == 'decorator_fixture'

def test_creates_blockspring_function(wrapped,request, response):
    assert response.result['_blockspring_spec']==True
    
def test_adds_output(wrapped, request, response):
    test = wrapped(request, response)
    assert response.result['output']==4

def test_wraps_functions_that_returns_dicts(dict_output_wrapped, request, response):
    test = dict_output_wrapped(request, response)
    assert response.result['output']['b_squared']==9

def test_wraps_functions_that_return_lists(list_output_wrapped, request, response):
    test = list_output_wrapped(request, response)
    assert response.result['output'][1]==9
