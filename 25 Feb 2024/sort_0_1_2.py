def sort012(arr, n):
    low, mid, high = 0, 0, n -1

    while mid <= high:

        if arr[mid] == 0:
            arr[mid], arr[low] = arr[low], arr[mid]
            mid += 1
            low += 1
        
        elif arr[mid] == 1:
            mid += 1
        
        else:
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1

a = [0, 2, 1, 2, 0]

sort012(a, len(a))

print(a)