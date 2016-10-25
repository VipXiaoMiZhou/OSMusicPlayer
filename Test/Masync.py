'''
Created on Oct 21, 2016

@author: zhangxing
'''
import asyncio

@asyncio.coroutine
def crawl_comments(furture):
    for i in range(1,10):
        print('A','crawl_comments',i)
        yield from asyncio.sleep(1)
    furture.set_result('A Over')

@asyncio.coroutine
def crawl_annotations(furture):
    for i in range(20,30):
        print('C','crawl_annotations',i)
        yield from asyncio.sleep(2)
    furture.set_result('B Over')
    

@asyncio.coroutine
def crawl_reviews(furture):
    for i in range(40,50):
        print('B','crawl_reviews',i)
        yield from asyncio.sleep(0.5)
    furture.set_result('C Over')

@asyncio.coroutine
def crawl_book(furture):
    for i in range(60,70):
        print('D','crawl_book',i)
        yield from asyncio.sleep(0.5)
    furture.set_result('D Over')



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    annotation_future = asyncio.Future()
    book_future = asyncio.Future()
    review_future = asyncio.Future()
    comment_future = asyncio.Future()
    tasks = [
             asyncio.ensure_future(crawl_book(book_future)),
             asyncio.ensure_future(crawl_comments(comment_future)),
             asyncio.ensure_future(crawl_reviews(review_future))
             ]
    loop.run_until_complete(asyncio.gather(*tasks))
    print(annotation_future.result())
    print(book_future.result())
    print(review_future.result())
    print(comment_future.result())
    loop.close()
