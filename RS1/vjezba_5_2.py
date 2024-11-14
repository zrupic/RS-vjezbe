# Izračun faktorijela s while petljom

broj = int(input("Unesite broj za izračun faktorijela: "))
faktor = 1
i = 1

while i <= broj:
    faktor *= i
    i += 1
print(f"Faktorijel broja {broj} je {faktor}")
