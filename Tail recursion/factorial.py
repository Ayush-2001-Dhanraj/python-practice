def factorial(num, fact =  1):
    if num < 0:
        return None
    
    if num == 1 or num == 0:
        return fact
    
    return factorial(num-1, num * fact)

