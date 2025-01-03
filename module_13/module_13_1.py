import asyncio
import time

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for i in range (1, 6):
        print(f'Силач {name} поднял {i} шар')
        await asyncio.sleep(10/power)
    print(f'Силач {name} закончил соревнования')

async def main():
    task = asyncio.create_task(start_strongman('Pasha', 3))
    task1 = asyncio.create_task(start_strongman('Denis', 4))
    task2 = asyncio.create_task(start_strongman('Apollon', 5))
    await task
    await task1
    await task2

start = time.time()
asyncio.run(main())
finish = time.time()

print(f'Соревнование закончено за {round(finish - start, 2)} минут')
