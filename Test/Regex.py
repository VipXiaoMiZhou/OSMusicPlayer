'''
Created on Oct 17, 2016

@author: zhangxing
'''
import re

#<a href="https://book.douban.com/subject/24736805/" title="erert"
patterm=re.compile(r'https://book.douban.com/subject/\d+',)
matcsh=patterm.findall('<a href="https://book.douban.com/subject/24736805/" title="erert')
print(matcsh)

if __name__ == '__main__':
    pass