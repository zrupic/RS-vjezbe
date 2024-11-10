# Unos brojeva
prvi_br=float(input("Unesite broj: "))
drugi_br=float(input("Unesite jos jedan broj: "))
r_radnja=input("Odaberite mat. radnju (+,-,/ ili *): ") 

#Izvedba radnje
if r_radnja=='+':
    print(f"Rezultat operacije: {prvi_br + drugi_br}")
elif r_radnja == '-':
    print(f"Rezultat operacije: {prvi_br - drugi_br}")
elif r_radnja == '*':
    print(f"Rezultat operacije: {prvi_br * drugi_br}")
elif r_radnja == '/':
    print("Greška: Dijeljenje s nulom nije dozvoljeno!" if drugi_br == 0 else f"Rezultat operacije: {prvi_br / drugi_br}")
else:
    print("Nepodržani operator")