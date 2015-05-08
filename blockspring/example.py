import blockspring

@blockspring.decorate
def fibonacci(x):
    """This will be the test function for our decorator"""
    print "doing something"+x
    x = int(x)
    if x < 0:
        raise ValueError('Must be greater than 0')
    elif x == 0:
        return 1
    elif x == 1:
        return 1
    else:
        return x*x 


def blibonacci(request, response):
    x = request.params['x']
    output = fibonacci(x)
    response.addOutput('output', output)
    response.end()

    
blockspring.define(fibonacci)
