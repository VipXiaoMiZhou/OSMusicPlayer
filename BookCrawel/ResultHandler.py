'''
Created on Nov 24, 2016

@author: zhangxing
'''

import DB

id = 0
def comments_handler(comments):
    if comments == '':
        return

    bookid = comments['bookid']

    for item in comments['comment-info']:
        commentor = item['commentator']
        commentator_homepage = item['commentator_homepage']
        comment_content = item['comment_content']
        comment_date = item['comment_date']
        comment_vote = item['comment_vote']
        star = item['star']
        sql = 'INSERT INTO comments VALUES ('+id+','+bookid+','+'\''+commentor+'\','+'\''+commentator_homepage+'\','+'\''+comment_content+'\','+comment_vote+','+'\''+comment_date+'\','+star+');'
        DB.execute(sql)
        id +=1
    pass


def url_handler(url):
    if url == ' ' or len(url) == 0:
        return

    for item in url:
        sql = 'INSERT INTO url VALURS('+url+');'
        DB.execute(sql)
    pass

def ebook_handler(ebook):
    if len(ebook) == 0:
        return

    bookid = ebook['bookid']
    for item in ebook:
        pass


def buy_handler(buy):

    if len(buy) == 0:
        return

    bookid = buy['bookid']


    pass


def bookinfo_handler(bookinfo):
    pass

def annotation_handler(annotation):
    if len(annotation) == 0:
        return

    bookid = annotation['bookid']
   
    for item in annotation['annotations']:
        user = item['user']
        user_pic = item['homepage']
        content = item['content']
        star = item['star']
        avatar = item['avatar']
        date = item['date']

    pass



def ip_handler(ip):
    pass


id = '200'
bookid = '123'
commentor= 'eason'
commentator_homepage = 'www.sina.com.cn'
comment_content = 'you raise me up'
comment_vote = '132456'
comment_date = '2012-5-30'
star = '100'

sql = 'INSERT INTO comments VALUES ('+id+','+bookid+','+'\''+commentor+'\','+'\''+commentator_homepage+'\','+'\''+comment_content+'\','+comment_vote+','+'\''+comment_date+'\','+star+');'

DB.execute(sql)
