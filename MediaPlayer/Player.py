# super class of player
class Player(Player):
    # play the song
    del play():
        Player.play()
        print "playing"
    # pause
    del pause():
        Player.pause()
        print "pause"
    #stop
    del stop():
        Player.stop()
        print "stop"
