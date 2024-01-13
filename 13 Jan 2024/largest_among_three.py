def get_largest(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3:
        return num2
    else:
        return num3

num1 = float(input("Number 1: "))
num2 = float(input("Number 2: "))
num3 = float(input("Number 3: "))

print(f"Largest amount {num1} | {num2} | {num3} -:- {get_largest(num1, num2, num3)}")