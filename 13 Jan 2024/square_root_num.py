from math import sqrt

def get_square_root(num):
    return num ** 0.5

def get_sqrt_using_math_mod(num):
    return sqrt(num)

num = float(input("Number: "))

print(f"\nSqrt using exponential: {get_square_root(num)}")
print(f"Sqrt using Math module: {get_sqrt_using_math_mod(num)}\n")