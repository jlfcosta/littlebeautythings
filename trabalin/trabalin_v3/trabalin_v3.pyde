import random as rd

t = 0
p = PVector(26, 874)
v = PVector(0, 0)
a = PVector(0, 0)

B = []

def setup():
    size(900, 900)
    
def draw():
    global t, p, v, a, B
    t += 0.03
    
    p.add(v*t)
    p.y += 0.5*a.y*t*t
    
    if p.y >= 875 or p.x <= 25 or p.x >= 875:
        t = 0
        p = PVector(26, 874)
        v *= 0
        a *= 0
    
    background(160)
    noStroke()
    fill(255)
    circle(p.x, p.y, 50)
    
    if a.y == 0:
        m = PVector(mouseX - p.x, mouseY - p.y).normalize()
        j = PVector(mouseX - p.x, mouseY - p.y).normalize().rotate(0.7853981)
        k = PVector(mouseX - p.x, mouseY - p.y).normalize().rotate(5.4977871)
        m *= 45
        j *= 20
        k *= 20
        
        fill(255)
        triangle(p.x + m.x, p.y + m.y, p.x + j.x, p.y + j.y, p.x + k.x, p.y + k.y)
    
    if frameCount%200 == 0:
        bombinha()
    
    for i in B:
        i[1] += 1
        fill(0)
        circle(i[0], i[1], 10)
        
        if ((p.x - i[0])**2 + (p.y - i[1])**2)**0.5 <= 30:
            t = 0
            p = PVector(26, 874)
            v *= 0
            a *= 0
            
            B.remove(i)
            
        if i[1] >= height:
            background(160)
            textSize(120)
            text("hehe, morreu", 10, 450)
            
    if frameCount <= 1000:
        textSize(20)
        fill(255)
        text("you,", 450, 450)
        text("after buying a missile launcher,", 450, 480)
        text("may protect yourself...", 450, 510)
        text("FROM OTHERS MISSILE LAUNCHERS!!!", 450, 540)
            
def mouseClicked():
    global t, p, v, a
    if a.y == 0:
        t = 0
        v = PVector(mouseX - p.x, mouseY - p.y).normalize()*14
        a.y = 9.8
        
def bombinha():
    global B
    n = rd.randint(5, width - 4)
    B.append([n, -5])