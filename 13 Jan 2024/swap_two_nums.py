def swap_using_third_val(val1, val2):
    temp = val1[0]
    val1[0] = val2[0]
    val2[0] = temp

def swap_without_third_val(val1, val2):
    val1[0], val2[0] = val2[0], val1[0]

val1 = [input("Variable 1: ")]
val2 = [input("Variable 2: ")]

swap_using_third_val(val1, val2)

print(f"Using third variable-\n val1: {val1[0]} | val2: {val2[0]}")

swap_without_third_val(val1, val2)

print(f"Without third variable-\n val1: {val1[0]} | val2: {val2[0]}")