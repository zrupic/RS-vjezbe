from aiohttp import web
app = web.Application()
proizvodi= [
    {"naziv": "banana", "cijena": 2, "količina": 10},
    {"naziv": "jabuka", "cijena": 1, "količina": 30},
    {"naziv": "šljiva", "cijena": 3, "količina": 20},
]
async def get_proizvodi(request):
    return web.json_response(proizvodi)

app.router.add_get('/proizvodi', get_proizvodi)

web.run_app(app, port=8081)