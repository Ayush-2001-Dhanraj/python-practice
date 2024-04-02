from sys import maxsize

def get_sub_array_max_sum(arr):
    max_sum = -maxsize - 1
    current_sum = 0

    for num in arr:

        current_sum += num

        if current_sum > max_sum:
            max_sum = current_sum

        if current_sum < 0:
            current_sum = 0
    
    return max_sum

a = [1,2,3,-2,5]

print(get_sub_array_max_sum(a))
print(get_sub_array_max_sum([-1,-2,-3,-4]))