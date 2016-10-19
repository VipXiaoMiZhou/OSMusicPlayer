import asyncio
import datetime

async def display_date(loop):
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)
    print('ha')




async def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    await asyncio.sleep(1.0)
    return x + y

async def print_sum(x, y):
    result = await compute(x, y)
    print("%s + %s = %s" % (x, y, result))

@asyncio.coroutine
def dtest():
    print('dTest')
    result= yield from print_sum(10, 20)
    
    
    print(result)
    return 'dTest'

async def sTet():
    print('sTet')
    result = await dtest()
    print(result)


loop = asyncio.get_event_loop()
# Blocking call which returns when the display_date() coroutine is done
loop.run_until_complete(display_date(loop))
loop.run_until_complete(print_sum(11, 20))

loop.run_until_complete(dtest())

loop.run_until_complete(sTet())
# future=asyncio.Future()
# asyncio.ensure_future(slow_operation(future))
# loop.run_until_complete(future)

loop.close()