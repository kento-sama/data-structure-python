my_list = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]

def bubble_sort(unordered_list):
    size = len(unordered_list)
    while size > 0:
        for i in range(size - 1):
            if unordered_list[i] > unordered_list[i + 1]:
                unordered_list[i], unordered_list[i + 1] = unordered_list[i + 1], unordered_list[i]
        size -= 1
        print(unordered_list)
        
bubble_sort(my_list)
