from aiohttp import web
import asyncio
import aiohttp

proizvodi = [
    {"id": 1, "naziv": "Laptop", "cijena": 5000},
    {"id": 2, "naziv": "Miš", "cijena": 100},
    {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
    {"id": 4, "naziv": "Monitor", "cijena": 1000},
    {"id": 5, "naziv": "Slušalice", "cijena": 50},
]

async def get_proizvodi(request):
    return web.json_response(proizvodi)

async def get_proizvod_by_id(request):
    proizvod_id = int(request.match_info.get('id'))
    proizvod = next((p for p in proizvodi if p["id"] == proizvod_id), None)
    if proizvod:
        return web.json_response(proizvod)
    else:
        return web.json_response(
            {"error": "Proizvod s traženim ID-em ne postoji"},
            status=404
        )

async def main():
   
    app = web.Application()
    app.router.add_get('/proizvodi', get_proizvodi)
    app.router.add_get('/proizvodi/{id}', get_proizvod_by_id)
    
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8081)
    await site.start()

    print("Server running on http://localhost:8081")
    
  
    async with aiohttp.ClientSession() as session:
        
        async with session.get('http://localhost:8081/proizvodi') as response:
            print("GET /proizvodi:")
            print(await response.json())

        async with session.get('http://localhost:8081/proizvodi/1') as response:
            print("\nGET /proizvodi/1 (postojeći proizvod):")
            print(await response.json())

        async with session.get('http://localhost:8081/proizvodi/10') as response:
            print("\nGET /proizvodi/10 (nepostojeći proizvod):")
            print(response.status)
            print(await response.json())

asyncio.run(main())