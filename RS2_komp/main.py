from shop.proizvodi import proizvodi, dodaj_proizvod
from shop.narudzbe import napravi_narudzbu

novi_proizvodi = [
    {"naziv": "Tipkovnica", "cijena": 200, "kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "kolicina": 100}
]

for proizvod in novi_proizvodi:
    dodaj_proizvod(proizvod)

print("Popis proizvoda:")
for proizvod in proizvodi:
    proizvod.ispis()

lista_narudzba = [
    {"naziv": "Laptop", "cijena": 5000, "kolicina": 2},
    {"naziv": "Monitor", "cijena": 1000, "kolicina": 1}
]

narudzba = napravi_narudzbu(lista_narudzba)

if narudzba:
    narudzba.ispis_narudzbe()
