def text_circle(rad, ch='*'):
    xscale = 4.2
# Maximum dismeter, plus a litter padding
    width = 3 + int(0.5 + xscale * rad)
    rad2 = rad ** 2
    for y in range(-rad,rad + 1):
        x = int(0.5 + xscale * (rad2- y ** 2) ** 0.5)
        s = ch * x
        print s.center(width)

for i in range(2, 15):
    print i
    text_circle(i)
