def check_leap_year(year):
    return "leap year" if (year % 400 == 0 and year % 100 == 0) or (year % 4 == 0 and year % 100 != 0) else "not leap year"

year = int(input("Year: "))
print(f"\n{year} is {check_leap_year(year)}\n")