import asyncio

async def dohvati_ko():
    print("Započinjemo s dohvaćanjem korisnika....")
    await asyncio.sleep(3)
    korisnici=[{"Ime i prezime: ", "Marko", "Markić "},
               {"Ime i prezime: ", "Ante", "Antić "},
               {"Ime i prezime: ", "Ivo", "Ivić "}]
    print("Korisnici dohvaćeni. ")
    return korisnici

async def dohvati_pro():
    print("Započinjemo s dohvaćanjem proizvoda....")
    await asyncio.sleep(5)
    proizvodi=[{"Naziv: ", "Laptop", " korištena"},
               {"Naziv: ", "Ekran", "novi"},
               {"Naziv: ", "Tipkovnica", "korištena"}]
    print("Proizvodi dohvaćeni!")
    return proizvodi
async def main():
    print("Započinjem konkurentno dohvaćanje podataka...")

    korisnici, proizvodi = await asyncio.gather(
        dohvati_ko(),
        dohvati_pro()
    )
    print(f"Dohvaćeni korisnici: {korisnici}")
    print(f"Dohvaćeni proizvodi: {proizvodi}")

asyncio.run(main())
