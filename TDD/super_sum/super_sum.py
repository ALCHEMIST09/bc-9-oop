def super_sum(*args):
    temp_list = []
    sum_total = 0
    
    if type(args[0]) == list and len(args) == 0:
        raise TypeError('Function expects a list of numbers, empty list passed')
    elif type(args) == None:
        raise TypeError('Function expects at least one argument. None passed')
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

print(super_sum([5, 6], [4,[5]], 10))
        