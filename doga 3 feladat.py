osszeg = float(input("adja meg a vásárlási összeget (Ft): "))

if osszeg < 10000:
    kedvezmeny = 0
    szazalek = 0
elif osszeg <= 20000:
    kedvezmeny = osszeg * 0.05
    szazalek = 5
else:
    kedvezmeny = osszeg * 0.10
    szazalek = 10

vegosszeg = osszeg - kedvezmeny

print(f"eredeti összeg: {osszeg:.0f} Ft")
print(f"kedvezmény: {szazalek}% ({kedvezmeny:.0f} Ft)")
print(f"fizetendő végösszeg: {vegosszeg:.0f} Ft")