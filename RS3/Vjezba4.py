import asyncio
import random

async def provjeri_parnost(broj):
    print(f"Provjeravam parnost za broj {broj}...")
    await asyncio.sleep(2)  
    if broj % 2 == 0:
        return f"Broj {broj} je paran."
    else:
        return f"Broj {broj} je neparan."


async def main():
    brojevi = [random.randint(1, 100) for _ in range(10)]
    print(f"Generirani brojevi: {brojevi}")

    zadaci = [provjeri_parnost(broj) for broj in brojevi]

    rezultati = await asyncio.gather(*zadaci)

    print("Rezultati:")
    for rezultat in rezultati:
        print(rezultat)

asyncio.run(main())
