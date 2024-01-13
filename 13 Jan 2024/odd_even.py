def check_odd_even(num):
    return "even" if num % 2 == 0 else "odd"

num = float(input("Number: "))
print(f"{num} is {check_odd_even(num)}")