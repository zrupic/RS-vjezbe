# broj koji treba pogoditi
broj = 33

# Bool varijabla
broj_je_pogoden = False

# Broj pokušaja
br_pokusaja = 0

while not broj_je_pogoden:
    pokusaj = int(input("Unesite broj između 1 i 100: "))
    br_pokusaja += 1 
    if pokusaj == broj:
        broj_je_pogoden = True
        print(f"Bravo, pogodio si iz {br_pokusaja} pokušaja!")
    elif pokusaj < broj:
        print("Broj je veći od unesenog. Pokušajte ponovno.")
    else:
        print("Broj je manji od unesenog. Pokušajte ponovno.")
