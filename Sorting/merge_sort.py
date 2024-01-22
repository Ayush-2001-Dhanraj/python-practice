def merge_sort(list):
    """
    Takes a list as input
    Returns sorted list

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous steps

    Takes overall O(kn log n) time
    Overal space complexity: O(n)
    """

    if len(list) <= 1:
        return list
    
    left_list, right_list = split(list)

    left = merge_sort(left_list)
    right = merge_sort(right_list)

    return merge(left, right)

def split(list):
    """
    find the midpoint of the list and return sublists divided by midpoints.

    Takes overall O(k log n) time K b/c in python slice operation is not O(1)
    it is O(k) where k is the no of elements under split 
    """
    mid = len(list) // 2
    return list[:mid], list[mid:]

def merge(left, right):
    """
    combine the left and right lists by taking smaller element first

    Takes overall O(n) time
    """
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
    
    while i < len(left):
        l.append(left[i])
        i += 1
    
    while j < len(right):
        l.append(right[j])
        j += 1
    
    return l

def verify_sort(list):
    if len(list) <= 1:
        return True
    
    return list[0] < list[1] and verify_sort(list[1:]) 
