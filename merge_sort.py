import random

my_list = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]

random_list = []
for i in range(25):
    while True:
        rand_num = random.randrange(0, 100)
        if rand_num not in random_list:
            random_list.append(rand_num)
            break
        
print(random_list)

def merge_sort(unordered_list):
    half = len(unordered_list) // 2
    if half < 1:
        return unordered_list
    first_list = merge_sort(unordered_list[:half])
    second_list = merge_sort(unordered_list[half:])
    
    i = 0
    j = 0
    orderered_list = []
    while i < len(first_list) or j < len(second_list):
        if i == len(first_list) and j < len(second_list):
            orderered_list.append(second_list[j])
            j += 1
            continue
        elif i < len(first_list) and j == len(second_list):
            orderered_list.append(first_list[i])
            i += 1
            continue
        
        if first_list[i] > second_list[j]:
            orderered_list.append(second_list[j])
            j += 1
        else:
            orderered_list.append(first_list[i])
            i += 1
    print(orderered_list)
    return orderered_list


merge_sort(random_list)
        
    
    
