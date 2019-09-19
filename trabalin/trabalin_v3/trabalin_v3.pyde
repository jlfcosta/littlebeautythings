t = 0
p = PVector(26, 874)
v = PVector(0, 0)
a = PVector(0, 0)

def setup():
    size(1800, 900)
    
def draw():
    global t, p, v, a
    t += 0.02
    
    p.add(v*t)
    p.y += 0.5*a.y*t*t
    
    if p.y >= 875 or p.x <= 25 or p.x >= 1775:
        t = 0
        p = PVector(26, 874)
        v *= 0
        a *= 0
    
    background(160)
    noStroke()
    fill(255)
    circle(p.x, p.y, 50)
    
def mouseClicked():
    global t, p, v, a
    if a.y == 0:
        t = 0
        v = PVector(mouseX - p.x, mouseY - p.y).normalize()*14
        a.y = 9.8
