def check_if_armstrong(num):
    order = len(str(num))
    temp = num
    sum = 0
    while temp > 0:
        rem = temp % 10
        sum += rem ** order
        temp = int(temp / 10)
    return True if sum == num else False

start = int(input("Armstrong in Interval\n Start: "))
end = int(input(" End: "))

for i in range(start, end + 1):
    if check_if_armstrong(i):
        print(f"{i}", end=" ")