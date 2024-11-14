# Izračun faktorijela s for petljom

broj = int(input("Unesite broj za koji izračunavate faktorijel: "))
faktor = 1

for i in range(1, broj + 1):
    faktor *= i

print(f"Faktorijel broja {broj} je {faktor}")
