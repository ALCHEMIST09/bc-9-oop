def my_sum(x, y):
    if x == None or y == None:
        raise TypeError('Function expects two positional arguments. One missing')
    if x == None and y == None:
        raise TypeError('Function expects two positional arguments. None given')
    else:
        return x + y

#my_sum(5, 20)

#def testFunc(a, b):
#    return a + b
#
#testFunc()


