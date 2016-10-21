#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2016-10-20
@author: Tiger Xie <xie_tiger@163.com>
'''

import requests
import json
from OSMusicPlayer.Logging.Logger import Log
import os
import urllib.request
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
        self.default_timeout = 3

    # 建立挖掘数据
    def build_dig(self, s, stype, limit=1):
        data = self.search(s, stype=stype, limit=limit)
        print(data)
        dig_data = []
        dig_type = ""

        if (stype == 1):
            song_ids = []
            for i in range(0, len(data['result']['songs']) ):
                song_ids.append( data['result']['songs'][i]['id'] )
            # 通过 ids 获得 songs 详细
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

    # 根据单曲 ids 获得单曲详细
    def songs_detail(self, ids, offset=0):
        action = 'http://music.163.com/api/song/detail?ids=[' + (',').join(map(str, ids)) + ']'
        try:
            data = self.httpRequest('GET', action)
#             print(data)
            return data['songs']
        except:
            return []

    # 根据专辑 id 获取单曲
    def alum_songs(self, alum_id):
        action = 'http://music.163.com/api/album/' + str(alum_id)
        try:
            data = self.httpRequest('GET', action)
            # log.info(data)
            return data['album']['songs']
        except:
            return []

    # 根据歌手 id 获得热门50单曲
    def artist_songs(self, artist_id):
        action = 'http://music.163.com/api/artist/' + str(artist_id)
        try:
            data = self.httpRequest('GET', action)
            # log.info(data)
            return data['hotSongs']
        except:
            return []

    # 根据歌手 id 获得专辑
    def artist_alums(self, artist_id, offset=0, limit=1):
        action = 'http://music.163.com/api/artist/albums/' + str(artist_id) + '?offset=' + str(offset) + "&limit=" + str(limit)
        try:

            data = self.httpRequest('GET', action)
            # log.info(data)
            return data['hotAlbums']
        except:
            return []

    # HTTP 请求
    def httpRequest(self, method, action, query=None):
        print(method, ' 请求')
        print('crawl: ', action)
        log.info('crawl: ' + action)

        connection = None
        if(method == 'GET'):
            connection = requests.get(action, headers=self.header, timeout=self.default_timeout)
        elif(method == 'POST'):

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
                timeout=self.default_timeout,
            )

        if connection is not None:
            log.info(connection.status_code)

            connection.encoding = "utf-8"
            connection = json.loads(connection.text)
            return connection
        else:
            return []

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

    # 下载音乐
    def download_mp3(self, song_info, save_dir):
        # 保存文件名： 歌名-歌手-专辑.mp3
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
        song_name = song_info['song_name']
        artist = '&'.join(str(a) for a in song_info['artist']) if type(song_info['artist']) is list else song_info['artist']
        album_name = song_info['album_name']
        file_name = song_name + '-' + artist + '-' + album_name + '.mp3'
        fpath = os.path.join(save_dir, file_name)
        log.info(fpath)
        if os.path.exists(fpath):
            return file_name + '已经下载过此mp3'

        # data_byte = requests.get(song_info['mp3_url']).text
        # file = open(fpath, 'wb')
        # file.write(data_byte)
        # file.close()

        try:
            urllib.request.urlretrieve(song_info['mp3_url'], fpath)
        except:
            return '由于版权保护，您所在的地区暂时无法下载'
        return file_name + '已经下载好了'