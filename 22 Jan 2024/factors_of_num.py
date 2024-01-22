from math import sqrt, ceil

def get_factors(num):
    factors = []
    # factors = list(filter(lambda x : num % x == 0 ,[x for x in range(1, ceil(sqrt(num)))]))
    for i in range(1, ceil(sqrt(num))):
        if num % i == 0:
            factors.append(i)
            if i != num // i:
                factors.append(num // i) 
    factors.sort()
    return factors

num = int(input("Numbers: "))
print(f"Factors: {get_factors(num)}")