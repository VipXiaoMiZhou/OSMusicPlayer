#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import wave
import sys
import pyaudio
from pygame import mixer as mp3   # mp3 playing module

__module_name__ = "MediaPlayer"
__author__ = "XiaoMiZhou"
__description__ = "This is a media audio player used to play songs from internet or native."
__date__ = "Tue Sep 27 4:11 PM"
__location__ = "Shanghai"


class WavAudioPlayer:
    CHUNK = 1024
    # instantiate PyAudio (1)
    p = pyaudio.PyAudio()


    def __init__(self,name,song):
        print "WavPlayer"
    def play(self,songurl):
        print "playing ",songurl
        pass
    def pause(self):
        print "pause"
        pass
    def stop(self):
        print "stop"
        pass
    @classmethod
    def description(self):
        print "WavPlayer Description"


class Mp3AudioPlayer:
    def __init__(self,name = 'mp3',song = 'XiXiHaHaXiaoMiZhou.mp3'):
        print "Mp3Player"
    def play(self,songurl):
        print "playing ",songurl
        pass

    def pause(self):
        print "pause"
        pass

    def stop(self):
        print "stop"
        pass

    @classmethod
    def description(self):
        print "Mp3Player Description"


class AudioPlayer:
    def __init__(self,name,song):
        self.name = name
        self.song = song
        print name

    def setType(self,t):
        self.type = t
    def getType(self):
        return self.type



    # play
    def play(self,url):
        if self.type == 'mp3':
            mp3 = Mp3AudioPlayer('Judy','Loving you.mp3')
            mp3.play(url)
        elif self.type == 'wav':
            wav = WavAudioPlayer('Candy','Hating you.mp3')
            wav.play(url)
        else:
            print "failed to play the file"

    # pause
    def pause(self):
        print "audio player pause"
    # stop
    def stop(self):
        print "audio player stop"
    @classmethod
    def description(self):
        print "description information"




sound = AudioPlayer('name','XiaoMiZhou.mp3')

sound.setType('mp3')
sound.getType()

sound.play('Lalalala.mp3')


sound.setType('wav')
sound.play('Loving you.mp3')


sound.setType('2')
sound.play('Hating you.mp3')





