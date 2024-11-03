

def cancellation(a, b):
    '''
    Copy elements one by one from input_list into output_list. 
    If one of the elements is equal to the stop_word, then stop the function,
    and return what you have so far.
    '''
    c = []
    for x in a:
        if x != b:
            c.append(x)
        else:
            return c
    return c

def copy_all_but_skip_word(a, b):
    '''
    This function should copy elements one by one from input_list into output_list.
    If one of the elements is equal to the skip_word, then you should skip that element,
    but keep checking all of the other elements.
    '''
    c = []
    for x in a:
        if x != b:
            c.append(x)
    return c

def my_average(a):
    '''
    You may assume that `input_list` is a non-empty list, in which every element is a number.  
    Calculate the average value, and return it. 
    '''
    d = 0
    c = 0
    if a != []:
        for x in a:
            if type(x) != str:
                c += x
                d += 1
            else:
                return None
        return c / d
    else:
        return None

