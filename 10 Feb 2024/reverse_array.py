def get_reversed(A):
    return A[::-1]

def get_rev_using_another_arr(A):
    if not len(A):
        return
    
    rev_A = []
    for i in range(len(A)):
        rev_A.insert(i, A[len(A) - i - 1])
    
    return rev_A

A = input()
A = list(map(int, A.split(" ")))
print(A)
print(get_reversed(A))
print(get_rev_using_another_arr(A))