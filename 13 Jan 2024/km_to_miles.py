def get_miles(kms):
    return kms * 0.621

kms = float(input("Kms: "))

print(f"{kms} kms = {get_miles(kms)} miles")