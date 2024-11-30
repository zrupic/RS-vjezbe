import asyncio

async def dohvati_po():
    print("Započinjemo s dohvaćanjem podataka....")
    await asyncio.sleep(3)
    podaci=[x for x in range(1, 11)]
    print("Podaci dohvaćeni. ")
    return podaci

async def main():
    podaci= await dohvati_po()
    print(f"Dohvaćeni podaci: {podaci}")

asyncio.run(main())    