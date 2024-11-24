class Narudzba:
    def __init__(self, proizvodi, ukupna_cijena):
        self.proizvodi = proizvodi
        self.ukupna_cijena = ukupna_cijena

    def ispis_narudzbe(self):
        proizvodi_ispis = ", ".join(f"{p['naziv']} x {p['kolicina']}" for p in self.proizvodi)
        print(f"Naručeni proizvodi: {proizvodi_ispis}, Ukupna cijena: {self.ukupna_cijena} eur")

def napravi_narudzbu(lista_proizvoda):
   
    if not isinstance(lista_proizvoda, list):
        print("Greška: Argument mora biti lista!")
        return None
    if not all(isinstance(p, dict) for p in lista_proizvoda):
        print("Greška: Svaki element mora biti rječnik!")
        return None
    if not all("naziv" in p and "cijena" in p and "kolicina" in p for p in lista_proizvoda):
        print("Greška: Svaki rječnik mora sadržavati ključeve 'naziv', 'cijena' i 'kolicina'!")
        return None
    if not lista_proizvoda:
        print("Greška: Lista ne smije biti prazna!")
        return None

    for p in lista_proizvoda:
        if p["kolicina"] <= 0:
            print(f"Proizvod {p['naziv']} nije dostupan!")
            return None

    ukupna_cijena = sum(p["cijena"] * p["kolicina"] for p in lista_proizvoda)

    narudzba = Narudzba(lista_proizvoda, ukupna_cijena)
    return narudzba
