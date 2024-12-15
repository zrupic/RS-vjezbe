import asyncio
import aiohttp

async def get_cat_fact(session):
    url="https://catfact.ninja/fact"
    async with session.get(url) as response:
        data=await response.json()
        return data.get("fact")
    
async def filter_cat_fact(facts):
    filter_facts= [fact for fact in facts if "cat" in fact.lower() or "cats" in fact.lower()] 
    return filter_facts   

async def main():
    async with aiohttp.ClientSession() as session:
        task=[get_cat_fact(session) for _ in range(20)]
        all_facts= await asyncio.gather(*task)
        filter_facts= await filter_cat_fact(all_facts)

        print( "Sve o mačkama")
        print(all_facts)
        print("\nFiltrirano sve o mačkama:")
        print(filter_facts)

asyncio.run(main())        