# from MusicSpider import NetEase
from OSMusicPlayer.Logging.Logger import Log
from OSMusicPlayer.NeteaseSpider.MusicSpider import NetEase
import os

netEase = NetEase()
log = Log.getLogger('NeteaseSpider')

# 搜索歌曲 stype=1
s = "imagine"
stype = 1
limit = 1

#  专辑 stype=10
# s = "Imagine"
# stype = 10
# limit = 1

# 歌手 stype=100
# s = "John Lennon"
# stype = 100
# limit = 1
dig_data, dig_type = netEase.build_dig(s, stype, limit)
print (dig_data)
print (dig_type)
log.info("==================被挖的数据================")
log.info(dig_data)

# 挖数据
log.info("==================挖数据结果================")
datalist = netEase.dig_info(dig_data, dig_type)
print(datalist)
log.info(datalist)

# 歌手专辑
log.info("==================歌手专辑================")
artist_alums = netEase.artist_alums('35333', limit=1)
print(artist_alums)
log.info(artist_alums)

# 专辑单曲
log.info("==================专辑单曲================")
alum_songs = netEase.alum_songs('2681093')
print(alum_songs)
# log.info(alum_songs)

# 歌手50首热门单曲
log.info("==================歌手50首热门单曲================")
artist_songs = netEase.artist_songs('35333')
print(artist_songs)
# log.info(artist_songs)
log.info("==================挖掘歌手50首热门单曲================")
dig_type = "songs"
datalist_hot = netEase.dig_info(artist_songs, dig_type)
print(datalist_hot)
# log.info(datalist_hot)

# 下载 mp3
pwd = os.path.abspath(os.path.dirname(__file__))
print(pwd)
result = netEase.download_mp3(datalist[0], pwd)
print(result)
log.info(result)
