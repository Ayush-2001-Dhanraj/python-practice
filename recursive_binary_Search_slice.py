def recursive_binary_Search_splice(list, target):
    """
    Returns True if target is in list else returns false
    """
    if len(list) == 0:
        return False
    else:
        mid = len(list) // 2
        if list[mid] == target:
            return True
        elif list[mid] > target:
            return recursive_binary_Search_splice(list[:mid], target)
        else:
           return recursive_binary_Search_splice(list[mid + 1:], target)
        
def verify(result):
    if(result):
        print('Target present in list')
    else:
        print('Target not present in list')

def convertToInt(num):
    return int(num)

list = list(map(convertToInt, input("Enter Elements seperated by ' ': ").split(" ")))
target = int(input("Enter target Element: "))
print(f"before sort list: {list}")
list.sort()
print(f"after sort list: {list}")
result = recursive_binary_Search_splice(list, target)
verify(result)