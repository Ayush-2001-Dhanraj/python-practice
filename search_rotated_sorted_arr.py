"""
problem statement: You are given list of numbers, obtained by rotating a 
sorted list an unknown number of times. 
Write a function to determine the minimum number of times 
the original sorted list was rotated to obtain the given list. 
Your function should have the worst-case complexity of O(log N),
 where N is the length of the list. 
 You can assume that all the numbers in the list are unique.

Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating 
the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.

We define "rotating a list" as removing the last element of the list and 
adding it before the first element. 
E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].

"Sorted list" refers to a list where the elements are arranged 
in the increasing order e.g. [1, 3, 5, 7].
"""

tests = [{'input': {'list': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]}, 'output': 3},
 {'input': {'list': [7, 9, 11, 14, 18, 3, 5, 6]}, 'output': 5},
 {'input': {'list': [1, 2, 3, 4, 5, 6, 7]}, 'output': 0},
 {'input': {'list': [7, 1, 2, 3, 4, 5, 6]}, 'output': 1},
 {'input': {'list': [7, 1, 2, 3, 4, 5, 6]}, 'output': 1},
 {'input': {'list': [1, 2, 3, 4, 5, 6, 7]}, 'output': 0},
 {'input': {'list': []}, 'output': -1},
 {'input': {'list': [6]}, 'output': -1},
 {'input': {'list': [5, 6, 6, 9, 9, 9, 0, 0, 2, 3, 3, 3, 3, 4, 4]}, 'output': 6},
 {'input': {'list': [3, 4, 4, 4, 5, 5, 6, 6 , 7, 7, 0, 0, 0, 0, 2, 3]}, 'output': 10}
 ]

def evaluateTests(alog, tests):
    for test in tests:
        print(test)
        actual = test['output']
        predicted = alog(**test['input'])
        print("actual: " , actual, "predicted: " , predicted)
        print("Result: ", actual == predicted, "\n")


def brute_force_find_rotations(list):
    position = 0
    while position < len(list):
        if position > 0 and list[position] < list[position - 1]:
            return position
        else:
            position += 1
    return -1 if len(list) <= 1 else 0

def check_condition(list, hi, mid):
    if mid > 0 and list[mid] < list[mid - 1]:
        return "found"
    elif list[mid] < list[hi]:
        # answer lies in left side
        return "left"
    else:
        # answer lies in right side
        return "right"

def binary_search_find_rotations(list):
    lo = 0
    hi = len(list) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        dir = check_condition(list, hi, mid)
        if dir == 'found':
            return mid
        elif dir == "left":
            hi = mid - 1
        else:
            lo = mid + 1
    return -1 if len(list) <= 1 else 0

# print("Brute force / Linear search approach")
# evaluateTests(brute_force_find_rotations, tests)

# print("Binary search approach")
# evaluateTests(binary_search_find_rotations, tests)

"""
You are given list of numbers, obtained by rotating a sorted list an 
unknown number of times. 
You are also given a target number. 
Write a function to find the position of the target number within 
the rotated list. 
You can assume that all the numbers in the list are unique.

Example: In the rotated sorted list [5, 6, 9, 0, 2, 3, 4], 
the target number 2 occurs at position 5.
"""

def firstMatch(cards, mid, query):
    if cards[mid] == query:
        if cards[mid] == cards[mid - 1]:
            return "left"
        else:
            return "found"
    elif cards[mid] > query:
        # move right
        return "right"
    else:
        # move left
        return "left"
    

def binary_search(cards, query):
    lo = 0
    hi = len(cards) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        condition = firstMatch(cards, mid, query)
        if condition == "found":
            return mid
        elif condition == "left":
            hi = mid - 1
        elif condition == "right":
            lo = mid + 1
    return -1

def search_in_rotated_list(list, target):
    rotations = binary_search_find_rotations(list)
    print("rotations", rotations)
    if rotations <= 0:
        print("in sinle")
        return binary_search(list, target)
    else:
        left_list = list[:rotations]
        right_list = list[rotations:]
        print("left_list",left_list)
        print("right_list",right_list)
        return max(binary_search(left_list, target), binary_search(right_list, target) + rotations + 1)
    
tests_search = [
    {'input': {'list': [5, 6, 9, 0, 2, 3, 4], 'target': 2}, 'output': 5},
    {'input': {'list': [5, 6, 9, 0, 2, 3, 4], 'target': 9}, 'output': 2},
]

evaluateTests(search_in_rotated_list, tests_search)