import sys
from loadFile import load_numbers

numbers  = load_numbers(sys.argv[1])

def selection_sort(list):
    sorted_list = []
    for j in range(len(list)):
        min_index = 0
        for i in range(len(list)):
            if list[i] < list[min_index]:
                min_index = i
        sorted_list.append(list.pop(min_index))
    return sorted_list

print(selection_sort(numbers))