import sys
from loadFile import load_numbers

numbers = load_numbers(sys.argv[1])

def quick_sort(list):
    if len(list) <= 1:
        return list
    
    left = []
    right = []
    pivot = list[0]

    for number in list[1:]:
        if number <= pivot:
            left.append(number)
        else:
            right.append(number)
    return quick_sort(left) + [pivot] + quick_sort(right)

sorted_list = quick_sort(numbers)
print(sorted_list)