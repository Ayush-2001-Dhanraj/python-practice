def check_num(num):
    if num > 0:
        return "+ve"
    elif num < 0:
        return "-ve"
    else:
        return "Zero"
    
def check_num_with_ternary(num):
    return "+ve" if num > 0 else "-ve" if num < 0 else "Zero"

num = float(input("Number: "))

print(f"\nif-else: {num} is {check_num(num)}")
print(f"ternary: {num} is {check_num_with_ternary(num)}\n")