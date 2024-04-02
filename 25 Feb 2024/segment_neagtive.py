def segment_negatives(arr, n):
    i = 0

    while i < n:
        if arr[i] < 0:

            j = i + 1

            while j < n and arr[j] < 0:

                j = j + 1
            
            if j < n :

                print(f"swapping {j} - {j - 1}")

                i = i - 1
                
                arr[j], arr[j - 1] = arr[j -1], arr[j]
            

        i += 1


def segment_negatives_faster(arr, n):

    pos = []
    neg = []

    for e in arr:
        if e < 0:
            neg.append(e)
        else:
            pos.append(e)

    posC = 0
    negC = 0
    
    while posC < len(pos):
        arr[posC] = pos[posC]
        posC += 1
    
    while negC < len(neg):
        arr[negC + posC] = neg[negC]
        negC += 1


a = [1, -1, 3, 2, -7, -5, 11, 6]

# segment_negatives(a, len(a))
segment_negatives_faster(a, len(a))

print(a)