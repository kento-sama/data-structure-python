def quick_sort(array, low=None, high=None):
    if low is None:
        low = 0
        high = len(array) - 1

    if low > high:
        return array
    
    lower_bound = low
    upper_bound = high
    
    # partitioning
    while low < high:
        if array[high] < array[low]:
            if high - low > 1:
                array[high - 1], array[high], array[low] = array[high], array[low], array[high - 1]
            else:
                array[low], array[high] = array[high], array[low]
            high -= 1
            print(array)
        else:
            low += 1
        
    quick_sort(array, lower_bound , high - 1)
    quick_sort(array, low + 1, upper_bound)
            
    return array

test = [22, 23, 38, 88, 42, 75, 44, 79, 21, 18, 61, 87, 99, 34, 77, 48, 63, 64, 56, 26, 60, 84, 80, 86, 57]
print(test)
print(quick_sort(test))
print(test)