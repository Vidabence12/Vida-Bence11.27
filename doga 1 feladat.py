import math

forma = input("Mit szeretnél kiszámítani? (kör/négyzet): ").lower().strip()

if forma == "kör":
    sugár = float(input("Adja meg a kör sugarát: "))
    terület = math.pi * sugár ** 2
    print(f"A kör területe: {terület:.2f} négyzetegység")

elif forma == "négyzet":
    oldal = float(input("Adja meg a négyzet oldalhosszát: "))
    terület = oldal ** 2
    print(f"A négyzet területe: {terület:.2f} négyzetegység")

else:
    print("érvénytelen választás! kérlek, írj be 'kör' vagy 'négyzet' szót.")