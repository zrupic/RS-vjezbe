class Proizvod:
    def __init__(self, naziv, cijena, kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.kolicina = kolicina

    def ispis(self):
        print(f"Naziv: {self.naziv}, Cijena: {self.cijena}, Količina: {self.kolicina}")

proizvodi = [
    Proizvod("Laptop", 5000, 10),
    Proizvod("Monitor", 1000, 20)
]

def dodaj_proizvod(novi_proizvod):
    proizvod = Proizvod(novi_proizvod["naziv"], novi_proizvod["cijena"], novi_proizvod["kolicina"])
    proizvodi.append(proizvod)
