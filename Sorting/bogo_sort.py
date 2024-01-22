import sys
from loadFile import load_numbers
import random

numbers = load_numbers(sys.argv[1])

def is_sorted(list):
    for i in range(0, len(list) - 1):
        if list[i] > list[i + 1]:
            return False
    return True

def bogo_sort(list):
    """
    luck based sorting - but technically not even sorting primarily shuffling
    """
    iterations = 0
    while not is_sorted(list):
        print(iterations)
        random.shuffle(list)
        iterations += 1

bogo_sort(numbers)
print(numbers)