from math import sqrt

def check_if_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        return True
    
    return False

start = int(input("Primes in Interval\n Start: "))
end = int(input(" End: "))

for i in range(start, end+ 1):
    if check_if_prime(i) :
        print(f"{i}", end=" ") 

