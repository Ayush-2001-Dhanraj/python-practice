start = int(input("Interval:\n start: "))
end = int(input(" end: "))

divisible_by = int(input("Check divisible by: "))

result = list(filter(lambda x: x % divisible_by == 0, [x for x in range(start, end + 1)]))

print(result)