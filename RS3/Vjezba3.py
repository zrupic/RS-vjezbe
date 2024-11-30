import asyncio
baza_korisnika = [
    {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
    {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
    {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
    {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
    {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
    {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
    {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
    {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]
async def autorizacija(korisnik_iz_baze, lozinka):
    print(f"Pokrećem autorizaciju za korisnika {korisnik_iz_baze['korisnicko_ime']}...")
    await asyncio.sleep(2)  
    lozinka_iz_baze = None
    for entry in baza_lozinka:
        if entry['korisnicko_ime'] == korisnik_iz_baze['korisnicko_ime']:
            lozinka_iz_baze = entry['lozinka']
            break  
    if lozinka_iz_baze == lozinka:
        return f"Korisnik {korisnik_iz_baze['korisnicko_ime']}: Autorizacija uspješna."
    else:
        return f"Korisnik {korisnik_iz_baze['korisnicko_ime']}: Autorizacija neuspješna."

async def autentifikacija(korisnik):
    print(f"Pokrećem autentifikaciju za korisnika {korisnik['korisnicko_ime']}...")
    await asyncio.sleep(3)  
    korisnik_iz_baze = None
    for entry in baza_korisnika:
        if entry['korisnicko_ime'] == korisnik['korisnicko_ime'] and entry['email'] == korisnik['email']:
            korisnik_iz_baze = entry
            break  
    if korisnik_iz_baze:
        print(f"Korisnik {korisnik['korisnicko_ime']} pronađen u bazi.")
        rezultat = await autorizacija(korisnik_iz_baze, korisnik['lozinka'])
        return rezultat
    else:
        return f"Korisnik {korisnik['korisnicko_ime']} nije pronađen."
async def main():
    # Promjena korisnika na mirko123
    korisnik = {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com', 'lozinka': 'lozinka123'}
    rezultat = await autentifikacija(korisnik)
    print(rezultat)

asyncio.run(main())