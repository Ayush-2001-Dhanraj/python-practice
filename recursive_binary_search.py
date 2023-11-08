def recursive_binary_search(list, target, start, end):
    """
    Recursively return index of target if it exists in list else none
    """
    mid = (start + end) // 2

    if not start <= end:
        return None
    elif list[mid] == target:
        return mid
    elif list[mid] > target:
        return recursive_binary_search(list, target, start, mid - 1) 
    else:
        return recursive_binary_search(list, target, mid + 1, end)

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
result = recursive_binary_search(list, target, 0, len(list) - 1)
verify(result)