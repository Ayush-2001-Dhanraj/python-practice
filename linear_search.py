def linear_search(list, target):
    """
    Returns index of target in list else none
    """

    for i in range(len(list)):
        if list[i] == target:
            return i
    
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
result = linear_search(list, target)
verify(result)