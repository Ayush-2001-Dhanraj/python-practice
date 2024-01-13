def get_c_to_f(c):
    return (c * (9 / 5)) + 32

c = float(input("Celsius: "))

print(f"{c} ℃  = {get_c_to_f(c)} ℉")