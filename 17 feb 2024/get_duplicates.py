def get_duplicates(nums):
    dict ={}

    for num in nums:
        dict[num] = dict.get(num, 0) + 1

    return [x[0] for x in dict.items() if x[1] > 1]

print(get_duplicates([1,1,1,3,3,4,3,2,4,2]))
print(get_duplicates([1,2,3,1]))
print(get_duplicates([1,2,3]))