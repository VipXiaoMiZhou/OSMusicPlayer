import urllib

from CrawFriends import URLManager
from CrawFriends import Requester
from CrawFriends import Disguiser
from urllib import request
from urllib.parse import *
from bs4 import BeautifulSoup

import re
import random

class Spider():
    pub_url_manager = URLManager()
    # https://book.douban.com/tag/%E9%9A%8F%E7%AC%94
    # loop = asyncio.get_event_loop()
    # annotation_future = asyncio.Future()
    # book_future = asyncio.Future()
    # review_future = asyncio.Future()
    # comment_future = asyncio.Future()

    @staticmethod
    def do_crawel(keyword, start, offset):
        Spider.crawl_url(keyword, start, offset)

    #         task = [
    #                 Spider.crawl_comments(keyword, start, offset,comment_future),
    #                 Spider.crawel_book(book_future)
    #                 ]
    #         pass

    @staticmethod
    # @asyncio.coroutine
    def crawel_book(keyword,furture = ''):
        keyword = str(keyword)
        url = 'https://book.douban.com/subject/' + keyword +'/'
        try:
            html_str = Requester.open_url(url)
        except Exception as e:
            print(e)
            print('Realoading...')
            html_str = Requester.open_url(url)
        
        def yield_f(html_str):
            book_info = {'title':'','cover_img':'','rank':'','vote':'',
                         'intro':'','vice_title':'','ori_title':'',
                         'author':'','press':'','press_year':'','pages':'',
                         'price':'','series':'','ISBN':'','transtor':'',
                         'binding':''
                        } 
            
            soup = BeautifulSoup(html_str,'lxml')    
                
            '''
            parse basic infos. Including book title,author,press,vote,rank etc.
            '''
            div = soup.find('div',id='mainpic')
            img = div.a['href']
            title = div.a['title']
            rank = soup.find('strong',class_='ll rating_num ').text
            vote_peple = soup.find('span',property = "v:votes").text
            
            book_info['title'] = title;
            book_info['cover_img'] = img
            book_info['rank'] = rank
            book_info['vote'] = vote_peple
            
            '''
            parse introductions
            '''
            def parse_intro(soup):
                div_intro = soup.find('div',id='link-report')
                span_intro= div_intro.find('div',class_='intro')
                for p in span_intro.find_all('p'):
                    book_info['intro'] = book_info['intro'] + p.text
                    
            '''
            parse infos.
            '''
            def parse_info(soup):
                if soup == '' : return 
                div_info = soup.find('div',id='info')
                infos = div_info.text 
                arr = []
                for info in infos.split('\n'):
                    info = str(info).strip()
                    if (len(info) < 1):
                        continue
                    else:
                        for item in info.split(':'):
                            if len(item) < 1:
                                continue
                            arr.append(item)
                
                def collect(arr):
                    if len(arr) < 1:
                        return
                    for i in range(0,len(arr)-1):
                        if arr[i] == u'作者':
                            i=i+1
                            book_info['author'] = arr[i]
                        elif arr[i] == u'出版社': 
                            i=i+1
                            book_info['press'] = arr[i]
                        elif arr[i] == u'丛书':
                            i=i+1
                            book_info['series'] = arr[i]
                        elif arr[i] == u'页数':    
                            i=i+1
                            book_info['pages'] = arr[i]
                        elif arr[i] == u'出版年':
                            i=i+1
                            book_info['press_year'] = arr[i]
                        elif arr[i] == u'装帧':
                            i=i+1
                            book_info['binding'] = arr[i]
                        elif arr[i] ==u'定价':
                            i=i+1
                            book_info['price'] = arr[i]
                        elif arr[i] == u'原作名':
                            i = i + 1
                            book_info['ori_title'] = arr[i]
                        elif arr[i] == u'译者' :
                            i = i + 1
                            book_info['transtor'] = arr[i]
                        elif arr[i] == u'ISBN' :
                            i = i + 1
                            book_info['ISBN'] = arr[i]
                        elif arr[i] == u'副标题':
                            i = i +1
                            book_info['vice_title'] = arr[i]
                        else:
                            pass
                collect(arr)
                
            

            percent = []            
            for item in soup.find_all('span',class_='rating_per'):
                percent.append(item.text)
            
            
            '''
            parse borrow infos.
            '''   
                   
            def parse_buyinfo(soup):
                borrow_info = []
                for item in soup.find_all('li',style='border: none'):
                    borrow = {'libary':'','borrow_link':''}
                    borrow['borrow_link'] = item.a['href']
                    borrow['libary'] = item.text   
                    borrow_info.append(borrow)
                    
                return borrow_info
             
            '''
            parse buy infos.
            '''
            
            def parse_borrowinfo(soup):
                buy_info = []
                div_buy = soup.find('div',id='buyinfo-printed')
                for li in div_buy.find_all('li'):
                    buy = {'website':'','url':'','price':'','discount':''}
#                 print(li)
                    buy_link = li.a['href']
                    span = li.find_all('span')
                
                    def getNum(str):
                        if str =='': return 0;
                        pattern = re.compile('\d+\.\d+', re.DOTALL)
                        result = pattern.findall(str)
                        if(len(result) > 0):return result[0]
                        else: return 0          
                    if len(span) > 0:
                        web_name = span[0].text
                    if len(span) > 2:
                        price = getNum(span[2].text)                    
                    if len(span) > 3:
                        discount = getNum(span[3].text)
            
                    buy['website'] = web_name
                    buy['url'] = buy_link
                    buy['price'] = price
                    buy['discount'] = discount
                    buy_info.append(buy)
                return buy_info
            
            parse_info(soup)
            parse_intro(soup)
            parse_borrowinfo(soup)       
            parse_buyinfo(soup)
            
            # 0 book_info 1 borrow_info  2 buy_info
            return(book_info,parse_borrowinfo(soup),parse_buyinfo(soup))   
        print(yield_f(html_str))

    @classmethod
    # @asyncio.coroutine
    def crawl_url(self, keyword, start, offset):
        # https://book.douban.com/subject/20427187/comments/hot?p=1
        if start == 0: start = 1
        if (start > offset) or (start < 0) or (offset < 0):
            print('Input  Illegal, Please Check Input and Run Again!')
            return
        while True:
            url = 'https://book.douban.com/tag/'+urllib.parse.quote(keyword)+'?start='+str((start - 1) * 20)+'&type=T'
            try:
                #                 html_str = Requester.open_url(url)
                #html_str = yield from Requester.open_url(url)
                html_str = Requester.open_url(url)
            except Exception as e:
                print(e)
                print('Reloading...')
                html_str = Requester.open_url(url)
            urls = re.findall(r"(?<=https://book.douban.com/subject/)\d+", html_str)
            #             print(urls)
            self.pub_url_manager.add_new_url(urls)
            start = start + 1
            if ((start - 1) * 20) > ((offset - 1) * 20):
                break

    #@classmethod
    # @asyncio.coroutine
    @staticmethod
    def crawl_comments( keyword, start, offset, furture):
        if keyword == '': return
        keyword = str(keyword)
        result = {'bookid': keyword, 'comment-info': []}
        while True:
            url = 'https://book.douban.com/subject/' + keyword + '/comments/hot?p=' + str(start)
            html_str = Requester.open_url(url)
            def yeld_f(html_str):
                soup = BeautifulSoup(html_str, 'lxml')
                for item in soup.find_all('li', class_="comment-item"):
                    info = {'commentator': '',
                            'avatar': '',
                            'commentator_homepage': '',
                            'comment_content': '',
                            'comment_date': '',
                            'comment_vote': '',
                            'star': ''
                            }
                    info['commentator'] = item.a['title']  # title
                    info['commentator_homepage'] = item.a['href']  # homepage
                    info['avatar'] = item.img['src']  # avatar image
                    info['comment_content'] = item.p.text  # comment_content

                    # comment date
                    comment_data = item.find_all(text=re.compile(r'\d{4}-\d{2}-\d{2}'))
                    if len(comment_data) > 0:
                        info['comment_date'] = comment_data[0].string
                    # vote_count
                    vote_count = item.find_all('span', class_='vote-count')
                    if len(vote_count) > 0:
                        info['comment_vote'] = vote_count[0].text
                    else:
                        info['comment_vote'] = 0

                    # start
                    # <span class="user-stars allstar50 rating" title="åè"></span>
                    star = item.find_all('span', class_=re.compile(r'(?<=allstar)\d+'))
                    if (len(star)) > 0:
                        z = star[0].attrs['class']  # ['user-stars','allstar50','rating']
                        if len(z) > 1:
                            point = z[1]
                            s = re.findall(r'\d+', point)  # ['50']
                            if len(s) >= 0:
                                info['star'] = s[0]  # 50
                            else:
                                info['star'] = 0
                                #                 print(info)
                                #                 resultx.append(info)
                    print(info)
                    result['comment-info'].append(info)

            # yield from yeld_f(html_str)
            yeld_f(html_str)
            start = start + 1
            if start > offset:
                print(result)
                # furture.set_result(result)
                break
        return result

    @staticmethod
    def crawl_annotations(keyword, start, offset):
        # https://book.douban.com/subject/20427187/annotation?sort=rank&start=0
        if keyword == '' or start > offset or start < 0:
            return
        keyword=str(keyword)
        result={'bookid':keyword,'annotations':[]}
        while True:
            url='https://book.douban.com/subject/'+keyword+'/annotation?sort=rank&start='+str((start-1)*10)
            html_str = Requester.open_url(url)
            def parse_html(html_str):
                soup = BeautifulSoup(html_str,'lxml')
                for item in soup.find_all('li',class_='ctsh clearfix'):
                    info = {'username': '',
                            'avatar': '',
                            'user_homepage': '',
                            'ananotation_content': '',
                            'ananotation_date': '',
                            'star': ''
                            }
                    # user link
                    user_url = item.find('div',class_='ilst').a['href']
                    # name
                    user_name = item.find('div',class_='ilst').img['alt']
                    #jgp 
                    user_pic = item.find('div',class_='ilst').img['src']
        
                    annotation = item.find('div',class_='all hidden').text
#                     print(annotation)
                    date_p = re.compile(r'\d{4}-\d{2}-\d{2}')
                    time_p = re.compile(r'\d{2}:\d{2}')
                    date =''
                    time =''
                    an=''
                    for str in annotation.split(' '):
                        if ' ' == str or '\n'==str or ''==str or '\r' == str:
                            continue
                        elif date_p.match(str) :
                            date = str
                            continue
                        elif time_p.match(str) :
                            time = str
                            continue
                        else:
                            an=an+str   
                    date = date + ' ' + time
                    annotation = an[:-28]
                    
                    info['username'] = user_name
                    info['avatar'] = user_pic
                    info['user_homepage'] =user_url
                    info['ananotation_content'] = annotation
                    info['ananotation_date'] = date
                    result['annotations'].append(info)          
            parse_html(html_str)
            
            start = start + 1
            if ((start - 1) * 10) > ((offset - 1) * 10):
                break
        print(result)
        return result
            
    @staticmethod
    def crawl_reviews(keyword, start, offset):
        # https://book.douban.com/subject/20427187/reviews?sort=hotest&start=20
        if keyword=='' or start > offset : return
        keyword=str(keyword)
        result={'bookid':'','reviews':[]}

        while True:
            url = 'https://book.douban.com/subject/' + keyword + '/reviews?sort=hotest&start=' + str(start)
            html_str=Requester.open_url(url)

            def parse_html(html_str):
                soup=BeautifulSoup(html_str,'lxml')
                pass

            pass
        pass


if __name__ == '__main__':
#     Spider.do_crawel('历史', 2, 10)
    Spider.crawel_book('20427187')
    Spider.crawel_book('26791257')
    Spider.crawel_book('25862578')
    Spider.crawel_book('4244848')
    Spider.crawel_book('3006581')
    Spider.crawel_book('1148282')
#     print(Spider.pub_url_manager.new_url)
    #
    #Spider.crawl_comments(1770782,1,5,'xsx')
#     Spider.crawl_annotations('20427187',2,3)
