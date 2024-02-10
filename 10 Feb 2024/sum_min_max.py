def sum_min_max(A, N):
    if not N:
        return
    max = min = A[0]
    for item in A:
        if min > item:
            min = item
        if max < item:
            max = item
    return max + min

A = input()
A = list(map(int, A.split(" ")))
print(sum_min_max(A, len(A)))