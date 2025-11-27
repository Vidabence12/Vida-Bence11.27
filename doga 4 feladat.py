import random

dobas1 = random.randint(1, 6)
dobas2 = random.randint(1, 6)

osszeg = dobas1 + dobas2

print(f"1. dobás: {dobas1}")
print(f"2. dobás: {dobas2}")
print(f"összeg: {osszeg}")

if osszeg > 9:
    print("nagy dobás!")
elif 6 <= osszeg <= 9:
    print("közepes dobás.")
else:
    print("kicsi dobás.") 