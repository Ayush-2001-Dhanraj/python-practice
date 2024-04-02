def get_max_Sum_positive_sub_array(arr):
    
    max_left = max_right = -1
    max_sum = current_sum  = 0
    current_left = 0

    for current_right in range(len(arr)):
        if arr[current_right] < 0:
            current_sum = 0
            current_left = current_right + 1

        else:
            current_sum += arr[current_right]

            if (current_sum > max_sum) or (current_sum == max_sum and current_right - current_left > max_right - max_left ) :
                max_sum = current_sum
                max_left = current_left
                max_right = current_right

    if max_left == -1 or max_right == -1:
        return -1
    
    return arr[max_left: max_right + 1]



print(get_max_Sum_positive_sub_array([1, 2, 5, -7, 2, 3, 8, -6, 16]))