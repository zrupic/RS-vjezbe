rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}

def obrni_rjecnik(rjecnik):
    rje={kljuc: vrijednost for kljuc, vrijednost in rjecnik.items()}
    return rje

print(obrni_rjecnik(rjecnik))