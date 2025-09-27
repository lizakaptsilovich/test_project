# import asyncio
#
# async def count():
#     print("One")
#     await asyncio.sleep(1)
#     print("Two")
#     await asyncio.sleep(1)
#
# async def main():
#     await asyncio.gather(count(), count(), count())
#
# if __name__ == "__main__":
#     import time
#
#     start = time.perf_counter()
#     asyncio.run(main())
#     elapsed = time.perf_counter() - start
#     print(f"{__file__} executed in {elapsed:0.2f} seconds.")

# import asyncio
#
# async def factorial(name, num):
#     f = 1
#     for i in range(2,num+1):
#         print(name)
#         await asyncio.sleep(0.1)
#         f = f * i
#     print(name, num, f)
#
# async def main():
#     await  asyncio.gather(factorial("A", 5), factorial("B",4), factorial("C", 3))
#
# asyncio.run(main())


# import os
# import re
# from datetime import datetime
#
# folder_path = "/Users/lizavetakaptsilovich/Documents/mom"
# files = [f for f in os.listdir(folder_path) if f.endswith(".xlsx")]
#
# # Функция для преобразования имени файла в datetime
# def file_to_date(file_name):
#     name = re.sub(r"\.xlsx$", "", file_name)
#     return name
#
# # сортировка по дате, от самой поздней к самой ранней
# files_sorted = sorted(files, key=file_to_date, reverse=True)
# files_display = [re.sub(r"\.xlsx$", "", f) for f in files_sorted]
#
# print(files_display)


# import asyncio
# import time
#
#
# async def fun1(x):
#     print(x**2)
#     await asyncio.sleep(3)
#     print('fun1 завершена')
#
#
# async def fun2(x):
#     print(x**0.5)
#     await asyncio.sleep(3)
#     print('fun2 завершена')
#
#
# async def main():
#     task1 = asyncio.create_task(fun1(4))
#     task2 = asyncio.create_task(fun2(4))
#
#     await task1
#     await task2
#
#
# print(time.strftime('%X'))
#
# asyncio.run(main())
#
# print(time.strftime('%X'))
# print(type(fun1))
#
# print(type(fun1(4)))




import asyncio
import time
from aiohttp import ClientSession


async def get_weather(city):
    async with ClientSession() as session:
        url = f'http://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}

        async with session.get(url=url, params=params) as response:
            weather_json = await response.json()
            print(f'{city}: {weather_json["weather"][0]["main"]}')


async def main(cities_):
    tasks = []
    for city in cities_:
        tasks.append(asyncio.create_task(get_weather(city)))

    for task in tasks:
        await task


cities = ['Moscow', 'St. Petersburg', 'Rostov-on-Don', 'Kaliningrad', 'Vladivostok',
          'Minsk', 'Beijing', 'Delhi', 'Istanbul', 'Tokyo', 'London', 'New York']

print(time.strftime('%X'))

asyncio.run(main(cities))

print(time.strftime('%X'))

