# -*- coding:utf-8 -*- 
'''
Created on Nov 24, 2016

@author: zhangxing
'''

import DB
from unittest.mock import _dot_lookup


_symbolAfter = '\','
_symbolBefore = '\''
_dot = ','

def comments_handler(comments):
    if comments == '' or len(comments) == 0:
        return
    for item in comments:
        bookid = item['bookid']
        user = item['user']
        avatar = item['avatar']
        content = item['content']
        homepage = item['homepage']
        star = item['star']
        vote = item['vote']
        c_date = item['c_date']
        commentsql = 'INSERT INTO COMMENTS(bookid,user,avatar,content,homepage,star,vote,c_date) VALUE ('+bookid+',\''+user+'\',\''+avatar+'\',\''+content+'\',\''+homepage+'\','+star+','+vote+',\''+c_date+'\');'
        DB.execute(commentsql)


def url_handler(url):
    if url == ' ' or len(url) == 0:
        return

    for item in url:
        sql = 'INSERT INTO url VALURS('+url+');'
        DB.execute(sql)
    pass


def buy_handler(buy):
    
    if len(buy) == 0 or buy == '':
        return
    for item in buy:
        bookid = item['bookid']
        website = item['website']
        url = item[ 'url']
        price = item['price']
        discount = item['discount']   
        sql = 'INSERT INTO BUYINFO(bookid,website,link,price,discount) VALUE ('+bookid+','+'\''+website+'\''+','+'\''+url+'\''+','+price+','+discount+');'
        DB.execute(sql)
        
def borrow_handler(borrow):
    if(len) == 0:
        return
    for item in borrow:
        bookid = item['bookid']
        libary = item['library']
        link = item['link']
        borrowsql = 'INSERT INTO BORROWINFO (bookid,library,link) VALUE ('+bookid+','+'\''+libary+'\','+'\''+link+'\');'
        DB.execute(borrowsql)
        
    pass


def bookinfo_handler(bookinfo):
    if bookinfo == '' or bookinfo is None:
        return
    
    bookid = bookinfo['bookid']
    title = bookinfo['title']
    cover_img = bookinfo['cover_img']
    rank = bookinfo['rank']
    vote = bookinfo['vote']
    intro = bookinfo['intro']
    author = bookinfo['author']    
    press = bookinfo['press']
    series = bookinfo['series']
    page = bookinfo['pages']
    press_year = bookinfo['press_year']
    binding = bookinfo['binding']
    ori_title = bookinfo['ori_title']
    transtor = bookinfo['transtor']
    ISBN = bookinfo['ISBN']
    vice_title = bookinfo['vice_title']
    price = bookinfo['price']
        
    sql = 'INSERT INTO BOOKINFO(bookid, title, cover_img, rank, vote, intro, vice_title, ori_title, author, press, press_year, pages, price, series, ISBN, transtor, binding) VALUE('
    sql +=_symbolBefore+bookid+_symbolAfter+_symbolBefore+title +_symbolAfter+_symbolBefore+cover_img+_symbolAfter
    sql +=rank+_dot+vote+_dot+_symbolBefore+intro+_symbolAfter+_symbolBefore+vice_title+_symbolAfter+_symbolBefore+ori_title+_symbolAfter
    sql += _symbolBefore+author+_symbolAfter+_symbolBefore+press+_symbolAfter+_symbolBefore+press_year+_symbolAfter+page+_dot+price+_dot
    sql +=_symbolBefore+series+_symbolAfter+_symbolBefore+ISBN+_symbolAfter+_symbolBefore+transtor+_symbolAfter+_symbolBefore+binding+'\');'
        
    print(sql)
    DB.execute(sql)
    sql = ''
    pass

def annotation_handler(annotation):
    if len(annotation) == 0:
        return
    
    # sql = 'INSERT INTO BUYINFO VALUE('1',12345,'tmall','www.eason.com',123.12,12.03);'
    
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


# id = '200'
# bookid = '123'
# commentor= 'eason'
# commentator_homepage = 'www.sina.com.cn'
# comment_content = 'you raise me up'
# comment_vote = '132456'
# comment_date = '2012-5-30'
# star = '100'
# price = '100'
# discount = '12'
# url = 'www.cctv.com'
# website = 'jd'
# name = 'msu'
# link = 'hahah.com'
# 
# 
# user = 'eason'
# avatar = 'you.jpg'
# content = 'you are not alone'
# homepage = 'you.com'
# star = '2'
# vote = '1546'
# c_date = '2012-12-12'
# 
# # sql = 'INSERT INTO comments VALUES ('+id+','+bookid+','+'\''+commentor+'\','+'\''+commentator_homepage+'\','+'\''+comment_content+'\','+comment_vote+','+'\''+comment_date+'\','+star+');'
# buysql = 'INSERT INTO BUYINFO(bookid,website,link,price,discount) VALUE ('+bookid+','+'\''+website+'\''+','+'\''+url+'\''+','+price+','+discount+');'
# print(buysql)
# # DB.execute(buysql)
# 
# 
# borrowsql = 'INSERT INTO BORROWINFO (bookid,library,link) VALUE ('+bookid+','+'\''+name+'\','+'\''+link+'\');'
# print(borrowsql)
# #DB.execute(borrowsql)
# 
# 
# 
# commentsql = 'INSERT INTO COMMENTS(bookid,user,avatar,content,homepage,star,vote,c_date) VALUE ('+bookid+',\''+user+'\',\''+avatar+'\',\''+content+'\',\''+homepage+'\','+star+','+vote+',\''+c_date+'\');'
# 
# print(commentsql)
# DB.execute(commentsql)

# bookid = '654321'
# title = 'Pride'
# cover_img = 'you.jpg'
# rank = '120'
# vote = '79465'
# intro = 'this is a lone lone story'
# vice_title = 'h'
# ori_title = 'ori'
# author = 'xxingzh'
# press = 'lala.pub'
# press_year = '2012-10-29'
# page = '200'
# price = '198.6'
# series = 'sdhfsi'
# ISBN = '566546546546'
# transtor = 'asd'
# binding = '546dsd'
# 
# sql = 'INSERT INTO BOOKINFO(bookid, title, cover_img, rank, vote, intro, vice_title, ori_title, author, press, press_year, pages, price, series, ISBN, transtor, binding) VALUE('
# sql +=_symbolBefore+bookid+_symbolAfter+_symbolBefore+title +_symbolAfter+_symbolBefore+cover_img+_symbolAfter
# sql +=rank+_dot+vote+_dot+_symbolBefore+intro+_symbolAfter+_symbolBefore+vice_title+_symbolAfter+_symbolBefore+ori_title+_symbolAfter
# sql += _symbolBefore+author+_symbolAfter+_symbolBefore+press+_symbolAfter+_symbolBefore+press_year+_symbolAfter+page+_dot+price+_dot
# sql +=_symbolBefore+series+_symbolAfter+_symbolBefore+ISBN+_symbolAfter+_symbolBefore+transtor+_symbolAfter+_symbolBefore+binding+'\');'
# 
# 
# print(sql)













