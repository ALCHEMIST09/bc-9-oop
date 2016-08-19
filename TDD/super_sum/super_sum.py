def super_sum(*args):
    temp_list = []
    sum_total = 0
    
    print(args)
    
    if len(args) == 0:
        raise TypeError('Function expects a list of numbers. None passed')
    elif len(args) == 1 and type(args[0]) == list and len(args[0]) == 0:
        '''
            Case of a single empty list
        '''
        raise TypeError('Function expects a list populated with integers. Empty list passed')
    else:
        for elem in args:
            if type(elem) == str:
                raise TypeError('Function expects number arguments. String passed')
        
        
    for item in args:
        if type(item) == type([]):
            for i in range(len(item)):
                temp_list.append(super_sum(item[i]))
        else:
            temp_list.append(item)
            
    for value in temp_list:
        sum_total += value
        
    return sum_total

# print(super_sum([5, 6], [4,[5]], 10))
        