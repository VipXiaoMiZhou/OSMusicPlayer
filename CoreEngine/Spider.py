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

    @classmethod
    # @asyncio.coroutine
    def crawel_book(self, furture):
        # yield from asyncio.sleep(1)
        pass

    @classmethod
    # @asyncio.coroutine
    def crawl_url(self, keyword, start, offset):
        # https://book.douban.com/subject/20427187/comments/hot?p=1
        if start == 0: start = 1
        if (start > offset) or (start < 0) or (offset < 0):
            print('Input  Illegal, Please Check Input and Run Again!')
            return
        data = {
            'action': 'https://book.douban.com/tag/',
            'tag': urllib.parse.quote(keyword),
            'start': 0,
            'type': 'T'
        }

        while True:
            data['start'] = (start - 1) * 20
            url = data['action'] + data['tag'] + '?start=' + str(data['start']) + '&type=' + data['type']
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

    @staticmethod
    def crawl_annotations(keyword, start, offset):
        # https://book.douban.com/subject/20427187/annotation?sort=rank&start=0
        if keyword == '' or start > offset or start < 0:
            return
        keyword=str(keyword)
        result={'bookid':'','annotations':[]}
        while True:
            url='https://book.douban.com/subject/'+keyword+'/annotation?sort=rank&start='+str((start-1)*10)
            html_str = Requester.open_url(url)
            def parse_html(html_str):
                soup = BeautifulSoup(html_str,'lxml')
                
                # annotions
#                 for item in soup.find_all('div',class_='all hidden'):
#                     print(item.a['href'])
#                     pass
                
                 
#                 for item in soup.find_all('p',class_='user'):
# #                     print(item)
#                     print(item.a['href']);
#                     print(item.a['title']);
#                     star = item.find_all('span', class_=re.compile(r'(?<=allstar)\d+'))
#                     if (len(star)) > 0:
#                         z = star[0].attrs['class']  # ['user-stars','allstar50','rating']
#                         if len(z) > 0:
#                             point = z[0]
#                             s = re.findall(r'\d+', point)  # ['50']
#                             if len(s) >= 0:
#                                 print(s[0])  # 50
#                             else:
#                                 print(0)
                
                for item in soup.find_all('li',class_='ctsh clearfix'):
                    
                    info = {'username': '',
                            'avatar': '',
                            'user_homepage': '',
                            'ananotation_content': '',
                            'ananotation_date': '',
                            'ananotation_vote': '',
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
                    star = item.find('span', class_=re.compile(r'(?<=allstar)\d+'))
                    
                    if (len(star)) > 0:
                        z = star[0].attrs['class']  # ['user-stars','allstar50','rating']
                        if len(z) > 0:
                            point = z[0]
                            s = re.findall(r'\d+', point)  # ['50']
                            if len(s) >= 0:
                                star = s[0] # 50
                            else:
                                star =0
                    print(star)
#                     print(annotation.split(' '))
                    an=''
                    date_p = re.compile(r'\d{4}-\d{2}-\d{2}')
                    time_p = re.compile(r'\d{2}:\d{2}')
                    date =''
                    time =''
                    for str in annotation.split(' '):
                        if ' ' == str or '\n'==str or ''==str:
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
                    
                    
#                     print(page)
                    
                    
                    
                    
                    
                    
                    
                    print(user_name)
                    print(user_pic)
                    print(user_url)
                    print(date)
                    print(annotation)
                    
                    print('>>>>>>>>>>>>>>>>>>>>>>')
#                    print(item.span)
                
            
                
            parse_html(html_str)
            start = start + 1
            if ((start - 1) * 10) > ((offset - 1) * 10):
                return

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
    # Spider.do_crawel('åå²', 2, 3)
    #
    #Spider.crawl_comments(1770782,1,5,'xsx')
    Spider.crawl_annotations('1770782',1,2)
