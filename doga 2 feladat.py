
helyes_nev = "admin"
helyes_jelszo = "1234"

nev = input("adja meg a felhasználónevet: ")
jelszo = input("adja meg a jelszót: ")

nev_helyes = (nev == helyes_nev)
jelszo_helyes = (jelszo == helyes_jelszo)

if nev_helyes and jelszo_helyes:
    print("sikeres bejelentkezés.")
elif not nev_helyes and jelszo_helyes:
    print("ismeretlen felhasználó.")
elif nev_helyes and not jelszo_helyes:
    print("hibás jelszó.")
else:
    print("helytelen adatok.")