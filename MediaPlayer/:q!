#! /usr/bin/python
# coding = utf-8

import time
import os
import sys
import string as s
import random as r
class UI:
    width = 50  # the width of player.
    height = 100 # the height of the player
    lace = '|' # lace
    def about(self):
        """ print infos on the screen

        """
        print '|`````````````````````````````````````````````````|'
        print '|                SuperMusicPlayer                 |'
        print '|                                                 |'
        print '| Author: xiaomizhou                              |'
        print '| Email : vipzhsh@163.com                         |'
        print '| Link  : https://github.com/VipXiaoMiZhou        |'
        print '|                                                 |'
        print '``````````````````````````````````````````````````'
    def search(self):
        """Get a string from input
        Returns:
            A string that from input.The string could be a song name,
            an album ,a singer stc.
        """
        name = raw_input('Search: ')
        return name

    def list(self):
# 1 means show current song list
        return 1
        pass
# 2 means switch next song
    def next(self):
        pass
# 3 means switch previres song
    def pre(self):
        pass
# 4 means playing the song
    def play(self):
        pass
# 5 means pausing the song
    def pause(self):
        pass
# 6 means stopimh the song
    def stop(self):
        pass
    def random(self):
        num = r.randint(0,65)
        return num

    def playUI(self):
        print '|`````````````````````````````````````````````````|'
        print '|                                                 |'
        print '|The love story  Tylor swift                      |'
        print '|[ ============================== >] 03:23/04:56  |'
        print '|                                                 |'
        print '| N [Next] P [Pre] S [Search] R [Random] L [List] |'
        print '``````````````````````````````````````````````````'

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

    def funcChooseUI(self):
        pre = '[Pre]'
        nxt = '[Next]'
        pause = '[Pause]'
        stop = '[Stop]'
        play = '[Play]'
        x = pre + ' ' + play + ' ' + nxt
        return UI.uiformater(x)

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
            m = int(float(process)/total * 40)
            return '['.ljust(m,'=') + '>]' + timeString(process,total).rjust(50-m)

        return bar(process, total)

x = UI()
# x.about()
# x.search()
# print x.random()
# x.face()
# x.face2('Dadi','Beyond')
# x.progressB(277,277)
print 'over'
print x.uiformater('`','`')
print x.uiformater(' ')
print x.audioInfoUI('Love Story.mp3','Tylor swift')
print x.funcChooseUI()
print x.uiformater('`','`')
for i in range(1,200):
    ds = x.progressBar(i,199)
    print '\r%s' %ds,
    sys.stdout.flush()
    time.sleep(0.1)
