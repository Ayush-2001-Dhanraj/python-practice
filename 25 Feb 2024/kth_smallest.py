import random


def kthSmallest(a, k):
    if len(a) <= 1:
        return a

    pivot = a[random.randint(0, len(a) - 1)]

    left = [x for x in a if x < pivot]
    right = [x for x in a if x > pivot]
    equal = [x for x in a if x == pivot]

    if k <= len(left):
        return kthSmallest(left, k)
    elif k <= len(left) + len(equal):
        return equal[0]
    else:
        return kthSmallest(right, k - len(left) - len(equal))   
    


a = [7 ,10, 4 ,3 ,20 ,15]

print(kthSmallest(a, 3))