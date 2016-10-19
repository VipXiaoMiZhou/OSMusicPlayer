import requests
import json
from OSMusicPlayer.Logging.Logger import Log
default_timeout = 3
log = Log.getLogger('NeteaseSpider')


class NetEase:
    def __init__(self):
        self.header = {
            'Accept': '*/*',
            'Accept-Encoding': 'deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,gl;q=0.6,zh-TW;q=0.4',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'music.163.com',
            'Referer': 'http://music.163.com/search/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36'
        }

    # biuld search
    def build_dig(self, s, stype, limit):
        data = self.search(s, stype=stype, limit=limit)
        print(data)
        dig_data = []
        dig_type = ""

        if (stype == 1):
            # 通过 ids 获得歌曲 songs 详细
            song_ids = []
            for i in range(0, len(data['result']['songs']) ):
                song_ids.append( data['result']['songs'][i]['id'] )
            dig_data = self.songs_detail(song_ids)
            dig_type = 'songs'

        elif (stype == 10):
            if 'albums' in data['result']:
                dig_data = data['result']['albums']
                dig_type = 'albums'

        elif (stype == 100):
            if 'artists' in data['result']:
                dig_data = data['result']['artists']
                dig_type = 'artists'

        return dig_data, dig_type

    # 搜索单曲(1)，专辑(10)，歌手(100)
    def search(self, s, stype=1, offset=0, total="true", limit=1):
        action = 'http://music.163.com/api/search/get/web'
        data = {
            's': s,
            'type': stype,
            'offset': offset,
            'total': total,
            'limit': limit
        }
        return self.httpRequest('POST', action, data)

    # song ids 拼接成 song urls 得到 details
    def songs_detail(self, ids, offset=0):
        action = 'http://music.163.com/api/song/detail?ids=[' + (',').join(map(str, ids)) + ']'
        print(action)
        try:
            data = self.httpRequest('GET', action)
#             print(data)
            return data['songs']
        except:
            return []

    # HTTP 请求
    def httpRequest(self, method, action, query=None):
        if(method == 'GET'):
            print('get 请求')
            url = action if (query == None) else (action + '?' + query)
            connection = requests.get(url, headers=self.header, timeout=default_timeout)

        elif(method == 'POST'):
            print('post 请求')
            # f = open("../Proxy/gnproxy")
            # lines = f.readlines()
            # proxys = []
            # for i in range(0,len(lines)):
            #     ip = lines[i].strip("\n").split("\t")
            #     proxy_host = "http://"+ip[0]+":"+ip[1]
            #     # print proxy_host
            #     proxy_temp = {"http":proxy_host}
            #     # print proxy_temp
            #     proxys.append(proxy_temp)
            #
            # for proxy in proxys:
            #     try:
            #         connection = requests.post(
            #             action,
            #             data=query,
            #             headers=self.header,
            #             timeout=default_timeout,
            #             proxies=proxy
            #         )
            #         log.info(proxy)
            #         log.info(connection.status_code)
            #         if (connection.status_code == 200):
            #             break
            #     except Exception as e:
            #         print (e)
            #         continue

            connection = requests.post(
                action,
                data=query,
                headers=self.header,
                timeout=default_timeout,
            )

        log.info(connection.status_code)

        connection.encoding = "utf-8"
        connection = json.loads(connection.text)
        return connection

    # 挖数据
    def dig_info(self, dig_data ,dig_type):
        temp = []
        
        if (dig_type == 'songs'):
            print('搜索歌曲')
            for i in range(0, len(dig_data) ):
                song_info = {
                    'song_id': dig_data[i]['id'],
                    'artist': [],
                    'song_name': dig_data[i]['name'],
                    'album_name': dig_data[i]['album']['name'],
                    'mp3_url': dig_data[i]['mp3Url']   
                }
                if 'artist' in dig_data[i]:
                    song_info['artist'] = dig_data[i]['artist']
                elif 'artists' in dig_data[i]:
                    for j in range(0, len(dig_data[i]['artists']) ):
                        song_info['artist'].append( dig_data[i]['artists'][j]['name'] )
                    song_info['artist'] = ', '.join( song_info['artist'] )
                else:
                    song_info['artist'] = '未知艺术家'

                temp.append(song_info)

        elif (dig_type == 'albums'):
            print('搜索专辑')
            for i in range(0, len(dig_data)):
                album_info = {
                    'album_id': dig_data[i]['id'],
                    'album_name': dig_data[i]['name'],
                    'artist_name': dig_data[i]['artist']['name'],
                }

                temp.append(album_info)

        elif (dig_type == 'artists'):
            print('搜索艺术家')
            for i in range(0, len(dig_data)):
                artist_info = {
                    'artist_id': dig_data[i]['id'],
                    'artist_name': dig_data[i]['name'],
                }

                temp.append(artist_info)

        return temp