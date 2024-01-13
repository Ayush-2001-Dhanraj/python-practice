def table_for_loop(num):
    for i in range(1, 11):
        print(f" {num} x {i} = {round(num * i, 1)}")

def table_while_loop(num):
    i = 1
    while i <= 10:
        print(f" {num} x {i} = {round(num * i, 1)}")
        i += 1

num = float(input("Number: "))
print("Using For : ")
table_for_loop(num)
print("Using  While : ")
table_while_loop(num)