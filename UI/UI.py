#! /usr/bin/python
# coding = utf-8

import time
import os
import sys
import json
import string as s
import random as r
class UI:
    width = 50  # the width of player.
    height = 100 # the height of the player
    lace = '|' # lace

    @classmethod
    def about(self):
        """ print infos on the screen
        """
        print '|`````````````````````````````````````````````````|'
        print '|                OSMusicPlayer                    |'
        print '|                                                 |'
        print '| Author: xiaomizhou                              |'
        print '| Email : vipzhsh@163.com                         |'
        print '| Link  : https://github.com/VipXiaoMiZhou        |'
        print '|                                                 |'
        print '``````````````````````````````````````````````````'

    @classmethod
    def help(self,hp):
        """ print helps
        Args:
            hp A json format collection.
            e.g {'N':'Next Play next song','S':'Stop Stop playing'}
        """
        print UI.uiformater('', '`')    # print top lace. e.g   `````````````````````````````````````````
        print UI.logo()                 # print logo info.
        print UI.uiformater(' ')        # print a black row

        for key in hp:
            print UI.uiformater(key + ' ' + hp[key])
        UI.lace = ''                  # change lace to ' '
        print UI.uiformater('', '`')  # print bottom lace
        UI.lace = '|'                 # recover lace


    def search(self):
        """Get a string from input
        Returns:
            A string that from input.The string could be a song name,
            an album ,a singer stc.
        """
        name = raw_input('Search: ')
        return name

    @classmethod
    def list(self,infolist):
        """print song list
        Args:
            infolist  a json string contains song infos.
        e.g:
        '[
            {
                "name": "QQmusic",
               " list": [
                            {
                                "singer": "John",
                                "song": "Doe"
                            },
                            {
                                "singer": "Anna",
                                "song": "Smith"
                            },
                            {
                                "singer": "Peter",
                                "song": "Jones"
                            }
                        ]
            }
        ]'
        """
        print UI.uiformater('', '`')    # print top lace. e.g   `````````````````````````````````````````
        print UI.logo()                 # print logo info.
        print UI.uiformater(' ')        # print a black row

        lists = json.loads(infolist)    # convert string to json obj

        length = len(lists)
        i = 0
        for l in lists:
           print UI.uiformater(l['name'])
           s = l['list']
           for ss in s:
               i = i + 1
               print  UI.uiformater('%d' %(i) + '   ' + ss['singer'] + '   ' + ss['song'])

        UI.lace = ''                  # change lace to ' '
        print UI.uiformater('', '`')  # print bottom lace
        UI.lace = '|'                 # recover lace




    @classmethod
    def uiformater(self, x, mark = ' '):
        """return a format ui string.
            Args:
                x  -- A string to be format.
            Returns:
                a format ui string.
        """
        ui = self.lace + x.ljust(self.width-2*len(self.lace),mark) + self.lace
        return ui


    def audioInfoUI(self,song, singer):
        x = song + ' ---- ' + singer
        return UI.uiformater(x)

    @classmethod
    def play(self, p):
        print UI.uiformater('', '`')    # print top lace. e.g   `````````````````````````````````````````
        print UI.logo()                 # print logo info.
        print UI.uiformater(' ')        # print a black row

        for key in p:
            print UI.uiformater(key + ' : ' + p[key])
        k = UI()
        UI.lace = ''                  # change lace to ' '
        print UI.uiformater('', '`')  # print bottom lace
        UI.lace = '|'                 # recover lace

    @classmethod
    def logo(self, logo = "OSMUSICPLAYER -0.0.1"):
        return UI.uiformater(logo)


    def funcChooseUI(self):
        pre = '[Pre]'
        nxt = '[Next]'
        pause = '[Pause]'
        stop = '[Stop]'
        play = '[Play]'
        x = pre + ' ' + play + ' ' + nxt + ' ' + stop
        return UI.uiformater(x)

class ProgressBar:
    # time.sleep(0.5)
    width = 50
    @classmethod
    def start(self,current, total):
        b = ProgressBar()
        z = b.progressBar(current,total)
        print '\r%s' %z,
        sys.stdout.flush()

    def stop(self):
        pass
    def pause(self):
        pass
    def progressBar(self,process,total):
        """Print a processbar on the console
        Args:
            process --An interge number that stand for the current process.
            totol   --An interge number that stand for the whloe process.
        Returns:
            A string of current proceaa bar.
            e.g:
            [ ============================== >] 03:23/04:56
        """

        def beautiLook(n):
            # make the number a better look.
            # e.g change 0 to 00
            if len(n) == 1:
                return '0' + n
            else:
                return n


        def timeString(process,total):
            """Composite a time string.
                    Calculate out current minutes and seconds from process number and Composite them into a whole string.
                    e.g:
                    02:54/04:24
                 Args:
                    process --An interge number that stand for the current process
                    totol   --An interge number that stand for the whloe process.
                Returns:
                    A string that show the process in time.
                    e.g:
                    10:02/15:10
            """
            # current time   minutes and seconds
            cm = beautiLook('%d' %(int(float(process)/60)))
            cs = beautiLook('%d' %(int(float(process)%60)))

            # total time  minutes and seconds
            tm = beautiLook('%d' %(int(float(total)/60)))
            ts = beautiLook('%d' %(int(float(total)%60)))
            return (cm + ':' + cs + '/' + tm + ':' + ts)


        def bar(process, total):
            """create a time bar """
            # current
            m = int(float(process)/total * self.width * 0.8)
            return '['.ljust(m,'=') + '>]' + timeString(process,total).rjust(self.width-m - 2)
        return bar(process, total)

if __name__ == '__main__':
    x = UI()
    p = ProgressBar()
    x.about()
    d = {'x':'fdfsdfsf', 'y':'asdasd', 'z':'asddd'}
    x.help(d)
    c = {'singer':'Kobe','song':'You are a gay','year':'2012.03.21','amblu':'tomorrrow'}
    x.play(c)
    l ='[{"name": "QQ music","list":[{"singer": "John","song": "Doe"},{"singer": "Anna","song": "Smith"},{"singer": "Peter","song": "Jones"}]}]'
    x.list(l)
    for i in range(0,200):
        p.start(i,199)
        time.sleep(0.1)
    x.search()
# print x.uiformater('`','`')
# print x.logo()
# print x.uiformater(' ')
