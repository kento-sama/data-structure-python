def binary_search(input_array, value):
    
    upper = len(input_array) - 1
    lower = 0
    while(upper >= lower):
        index = (lower + upper) // 2
        if input_array[index] > value:
            upper = index - 1
        elif input_array[index] < value:
            lower = index + 1
        else:
            return index
    
    return -1

def binary_search_rec(input_array, value, lower=None, upper=None):
    if lower is None:
        lower = 0
        upper = len(input_array) - 1
        
    if lower > upper:
        return - 1
    
    index = (lower + upper) // 2
    if input_array[index] > value:
        return binary_search_rec(input_array, value, lower, index - 1)
    elif input_array[index] < value:
        return binary_search_rec(input_array, value, index + 1, upper)
    else:
        return index


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))

print("------------")

print(binary_search_rec(test_list, test_val1))
print(binary_search_rec(test_list, test_val2))

