from aiohttp import web

app = web.Application()

proizvodi = [
    {"naziv": "banana", "cijena": 2, "količina": 10},
    {"naziv": "jabuka", "cijena": 1, "količina": 30},
    {"naziv": "šljiva", "cijena": 3, "količina": 20},
]

async def get_proizvodi(request):
    return web.json_response(proizvodi)

async def add_proizvod(request):
   
    novi_proizvod = await request.json()
    
    print(f"Primljeni podaci: {novi_proizvod}")
    
    proizvodi.append(novi_proizvod)
   
    return web.json_response(proizvodi)

app.router.add_get('/proizvodi', get_proizvodi)
app.router.add_post('/proizvodi', add_proizvod)

web.run_app(app, port=8081)
