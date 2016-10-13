import tty, sys, time
tty.setraw(sys.stdin.fileno())
while 1:
    ch = sys.stdin.read(1)
    time.sleep(1)
    print ch
