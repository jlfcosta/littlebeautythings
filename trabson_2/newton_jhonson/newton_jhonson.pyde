bolinhas = 3 # Quantidade de bolinhas.
blist = []
h = 0


def setup():
    global bolinhas, blist, h
    size(900, 900)
    h = height/3
    for i in range(bolinhas):
        blist.append([2*width/7 + 1/(
    
    
def draw():
    global bolinhas, h
    background(191)
    line(2*width/7, height/20, 5*width/7, height/20)
    line(2*width/7, 11*height/20, 5*width/7, 11*height/20)
    
def mousePressed():
    global blist
