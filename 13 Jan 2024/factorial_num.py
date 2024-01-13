def get_factorial_with_loop(num):
    if num < 0:
        return "undefined"
    fact = 1
    for i in range(2, num + 1):
        fact *= i
    return fact

def get_factorial_with_recursion(num):
    if num < 0:
        return "undefined"
    return 1 if num == 0 else num * get_factorial_with_recursion(num - 1)

num = int(input("Number: "))
print(f"\nFactorial of {num} : \n{get_factorial_with_loop(num)} | Loop")
print(f"{get_factorial_with_recursion(num)} | Recursion")