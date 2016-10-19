'''
Created on Oct 19, 2016

@author: zhangxing
'''
import asyncio

@asyncio.coroutine
def factorial(name, number):
    async def t():
        time.sleep(1)
    return 't'

    f = 1
    for i in range(2, number+10):
        print("Task %s: Compute factorial(%s)..." % (name, i))
#         result=yield from asyncio.sleep(1)
        result = await t()
        f *= i
    print("Task %s: factorial(%s) = %s" % (name, number, f))

loop = asyncio.get_event_loop()
tasks = [
    asyncio.ensure_future(factorial("A", 2)),
    asyncio.ensure_future(factorial("B", 3)),
    asyncio.ensure_future(factorial("C", 4))]
loop.run_until_complete(asyncio.gather(*tasks))
loop.close()