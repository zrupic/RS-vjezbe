import asyncio
import aiohttp

async def get_dog_fact(session):
    url="https://dogapi.dog/api/v2/facts"
    async with session.get(url) as response:
        data=await response.json()
        return data['data'][0]['attributes']['body']

async def get_cat_fact(session):
    url="https://catfact.ninja/fact"   
    async with session.get(url) as response:
        data=await response.json()
        return data['fact']
    
async def mix_facts(dog_facts, cat_facts):
    return [
        dog_fact if len(dog_fact) > len(cat_fact) else cat_fact
        for dog_fact, cat_fact in zip(dog_facts, cat_facts)
    ]
async def main():
    async with aiohttp.ClientSession() as session:
        dog_fact_task = [get_dog_fact(session) for _ in range(5)]
        cat_fact_task = [get_cat_fact(session) for _ in range(5)]
        all_facts= await asyncio.gather(*dog_fact_task, *cat_fact_task)

        dog_facts = all_facts[:5]
        cat_facts = all_facts[5:]
        filtered_facts = await mix_facts(dog_facts, cat_facts)

        print("Miješane činjenice o psima i mačkama:")
        for fact in filtered_facts:
            print(fact)

asyncio.run(main())            