import asyncio
import aiohttp
import time

async def fetch_users(session):
    url = "https://jsonplaceholder.typicode.com/users"
    async with session.get(url) as response:
        return await response.json()

async def main():
    start_time = time.time()  

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_users(session) for _ in range(5)]
        results = await asyncio.gather(*tasks)  

    users = results[0]  
    imena = [user['name'] for user in users]
    emailovi = [user['email'] for user in users]
    korisnicka_imena = [user['username'] for user in users]

    end_time = time.time()

    print("Imena korisnika:", imena)
    print("Email adrese korisnika:", emailovi)
    print("Korisnička imena:", korisnicka_imena)
    print(f"Vrijeme izvršavanja programa: {end_time - start_time:.2f} sekundi")

asyncio.run(main())
