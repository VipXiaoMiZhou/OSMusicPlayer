import urllib
import threading
import re

from CrawFriends import URLManager
from CrawFriends import Requester
from Parsers import BookInfoParser
from Parsers import CommentParser
from Parsers import AnnotationParser

lock = threading.Condition() 

class Spider():
      
    @staticmethod
    def crawel_book(keyword):
        keyword = str(keyword)
        parser = BookInfoParser()
        url = 'https://book.douban.com/subject/' + keyword +'/'
        try:
            html_str = Requester.open_url(url)
        except Exception as e:
            print(e)
            print('Realoading...')
            html_str = Requester.open_url(url)
        result = parser.parser(html_str, keyword)
        return html_str
        

    @staticmethod
    def crawl_url(keyword,start):
        # producer
        url = 'https://book.douban.com/tag/'+urllib.parse.quote(keyword)+'?start='+str((start - 1) * 20)+'&type=T'
        try:
            html_str = Requester.open_url(url)
        except Exception as e:
            print(e)
            print('Reloading...')
            html_str = Requester.open_url(url)
        urls = re.findall(r"(?<=https://book.douban.com/subject/)\d+", html_str)
        return urls

    @staticmethod
    def crawl_comments(keyword, start, offset, furture):
        if keyword == '': return
        keyword = str(keyword)
        parser = CommentParser()
        url = 'https://book.douban.com/subject/' + keyword + '/comments/hot?p=' + str(start)
        html_str = Requester.open_url(url)
        start = start + 1

    @staticmethod
    def crawl_annotations(keyword, start, offset):
        # https://book.douban.com/subject/20427187/annotation?sort=rank&start=0
        if keyword == '' or start > offset or start < 0:
            return
        keyword=str(keyword)
        url='https://book.douban.com/subject/'+keyword+'/annotation?sort=rank&start='+str((start-1)*10)
        html_str = Requester.open_url(url) 
        start = start + 1
        if ((start - 1) * 10) > ((offset - 1) * 10):
            return
            
    @staticmethod
    def crawl_reviews(keyword, start, offset):
        # https://book.douban.com/subject/20427187/reviews?sort=hotest&start=20
        if keyword=='' or start > offset : return
        keyword=str(keyword)
        url = 'https://book.douban.com/subject/' + keyword + '/reviews?sort=hotest&start=' + str(start)
        html_str=Requester.open_url(url)

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
