def fibbo_recursive(n):
    if n < 0:
        return None
    
    if n == 0:
        return 0
    
    if n == 1 or n == 2:
        return 1
    
    return fibbo_recursive(n-1) + fibbo_recursive(n-2)

def fibbo_tail_recursive(n, a = 0, b = 1):
    if n < 0:
        return None
    
    if n == 0:
        return a
    
    return fibbo_tail_recursive(n-1, b, a + b)