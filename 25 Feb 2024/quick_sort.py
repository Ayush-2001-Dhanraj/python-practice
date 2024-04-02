import random


def quick_sort(arr):

    if len(arr) <= 1:
        return arr
    
    pivot = random.randint(0, len(arr)-1)

    left = [x for x in arr if x < arr[pivot]]
    equal = [x for x in arr if x == arr[pivot]]
    right = [x for x in arr if x > arr[pivot]]

    return quick_sort(left) + quick_sort(equal) + quick_sort(right)
     
# a = [2, 10, 1, 6, 7, 9]
a = [7 ,10, 4 ,3 ,20 ,15]


print(quick_sort(a))