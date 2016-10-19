'''
Created on Oct 19, 2016

@author: zhangxing
'''
import asyncio

@asyncio.coroutine
def slow_operation(future):
    yield from asyncio.sleep(5)
    future.set_result('Future is done!')

def got_result(future):
    print(future.result())
    loop.stop()

loop = asyncio.get_event_loop()
future = asyncio.Future()
asyncio.ensure_future(slow_operation(future))
future.add_done_callback(got_result)
try:
    loop.run_forever()
finally:
    loop.close()