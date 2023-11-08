def binary_search(list, target):
    """
    Accepts sorted list.
    Returns Index of target if present else none
    """

    start = 0
    end = len(list) -1 
    while(start <= end):
        mid  = (start + end) // 2

        if list[mid] == target:
            return mid
        elif list[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None

def verify(index):
    if(index):
        print(f"Target found at index {index}")
    else :
        print("Target not found in the list")

def convertToInt(num):
    return int(num)

list = list(map(convertToInt, input("Enter Elements seperated by ' ': ").split(" ")))
target = int(input("Enter target Element: "))
print(f"before sort list: {list}")
list.sort()
print(f"after sort list: {list}")
result = binary_search(list, target)
verify(result)