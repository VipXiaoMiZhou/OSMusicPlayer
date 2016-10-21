'''
Created on Oct 20, 2016

@author: zhangxing
'''
from bs4 import BeautifulSoup
import re
# soup = BeautifulSoup('<span class="comment-info">'+
#                      '<a href="https://www.douban.com/people/89858646/">绿水兰木</a>'+
#                      '<span class="user-stars allstar50 rating" title="力荐"></span>'+
#                      '<span>2016-09-05</span>'+
#                      '</span>','lxml')
# line ='<span class="comment-info"><a href="https://www.douban.com/people/89858646/">绿水兰木</a><span class="user-stars allstar50 rating" title="力荐"></span><span>2016-09-05</span></span>'
# print(re.findall(r'\d{4}-\d{2}-\d{2}', line))
# print(re.findall(r'allstar\d{2}', line))
# print(soup.a.text)
# print(soup.a['href'])
html='''
<li class="comment-item">
<div class="avatar">
<a href="https://www.douban.com/people/89858646/" title="绿水兰木">
<img src="https://img3.doubanio.com/icon/u89858646-2.jpg"/>
</a>
</div>
<h3>
<span class="comment-vote">
<span class="vote-count" id="c-1071884064">0</span>
<a class="j a_show_login" data-cid="1071884064" href="javascript:;" id="btn-1071884064">有用</a>
</span>
<span class="comment-info">
<a href="https://www.douban.com/people/89858646/">绿水兰木</a>
<span class="user-stars allstar50 rating" title="力荐"></span>
<span>2016-09-05</span>
</span>
</h3>
<p class="comment-content">读过原版，再看中文版，真心觉得竺家荣老师翻译的太赞啦！</p>
</li>
'''
soup = BeautifulSoup(html,'lxml')
print(soup.a['title'])
print(soup.a['href'])
print(soup.img['src'])
s=soup.find_all('span',class_='vote-count')
print(re.findall(r'(?<=>)\d+','>0</span>'))
print(soup.p.text)
print(re.findall(r'\d{4}-\d{2}-\d{2}', html))
print(re.findall(r'(?<=allstar)\d+', 'user-stars allstar50 rating'))


