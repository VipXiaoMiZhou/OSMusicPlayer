#encoding=utf8
import urllib.request
from bs4 import BeautifulSoup

User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
header = {}
header['User-Agent'] = User_Agent

# url = 'http://www.xicidaili.com/nn/1' # 国内代理
url = 'http://www.xicidaili.com/wt/1'   # 国外代理
request = urllib.request.Request(url, headers=header)
res = urllib.request.urlopen(request).read().decode('utf-8')

soup = BeautifulSoup(res, 'html.parser')
ips = soup.findAll('tr')
# print(ips)
# 国内代理存入 gnproxy, 国外代理存入 gwproxy
# f = open("./gnproxy","w")
f = open("./gwproxy","w")

for x in range(1,len(ips)):
    ip = ips[x]
    tds = ip.findAll("td")
    ip_temp = tds[1].contents[0]+"\t"+tds[2].contents[0]+"\n"
    print (tds[1].contents[0]+"\t"+tds[2].contents[0])
    f.write(ip_temp)