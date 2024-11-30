import asyncio

async def secure_data(podaci):
    print(f"Započinjem enkripciju za prezime: {podaci['prezime']}...")
    await asyncio.sleep(3)  
    enkriptirani_podaci = {
        'prezime': podaci['prezime'],
        'broj_kartice': hash(podaci['broj_kartice']),
        'CVV': hash(podaci['CVV'])
    }
    print(f"Enkripcija dovršena za prezime: {podaci['prezime']}.")
    return enkriptirani_podaci


async def main():
    
    osjetljivi_podaci = [
        {'prezime': 'Ivić', 'broj_kartice': '1234-5678-9012-3456', 'CVV': '123'},
        {'prezime': 'Anić', 'broj_kartice': '2345-6789-0123-4567', 'CVV': '456'},
        {'prezime': 'Markić', 'broj_kartice': '3456-7890-1234-5678', 'CVV': '789'}
    ]

    zadaci = [secure_data(podaci) for podaci in osjetljivi_podaci]

    rezultati = await asyncio.gather(*zadaci)

    print("Enkriptirani podaci:")
    for rezultat in rezultati:
        print(rezultat)

asyncio.run(main())
