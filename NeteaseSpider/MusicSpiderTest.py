# from MusicSpider import NetEase
from OSMusicPlayer.Logging.Logger imort Log
from OSMusicPlayer.NeteaseSpider.MusicSpider import NetEase

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
#
# # 歌手 stype=100
# s = "John Lennon"
# stype = 100
# limit = 1
dig_data, dig_type = netEase.build_dig(s, stype, limit)
print (dig_data)
print (dig_type)
log.info("==================dig_data================")
log.info(dig_data)

# 挖歌曲中的数据
log.info("==================datalist================")
datalist = netEase.dig_info(dig_data, dig_type)
print(datalist)
log.info(datalist)