#declaração das variáveis iniciais
import random as rd
xmax = 1000
ymax = 580

r=20
p = PVector(r,ymax-r)
v = PVector(0,0)
vb = 0
wind = PVector(0,0)
a = PVector(0,0)
ab=9.8
t=.0
dt = 0.166666
B=[]
k2=0
K2=0
def setup():
    size(xmax,ymax)

def draw():
    global r, p, v, a, t, dt, B,wind,vb,K2,k2,ab
    print("tipo vb:{} k2={}...tipodt...{}tipoab..{}".format(type(vb),type(k2),type(dt),type(ab)))
    t+=dt
    p.x=r+v.x*t +0.5*a.x*t*t
    p.y=ymax-r+v.y*t+0.5*a.y*t*t
        
    
    
    background(0)
    fill(0,255,0)
    circle(p.x,p.y,2*r)
    # (Estética braba) Caso a bolinha branca não estiver se mexendo, uma setinha surge nela.
    if a.y == 0:
        m = PVector(mouseX - p.x, mouseY - p.y).normalize()
        j = PVector(mouseX - p.x, mouseY - p.y).normalize().rotate(0.7853981)
        k = PVector(mouseX - p.x, mouseY - p.y).normalize().rotate(5.4977871)
        m *= 45
        j *= 20
        k *= 20
        
        fill(0,255,0)
        noStroke()
        triangle(p.x + m.x, p.y + m.y, p.x + j.x, p.y + j.y, p.x + k.x, p.y + k.y)
    if frameCount%170 == 50:
        bombinha() # Função de construção das bolinhas pretas.
    for b in B:
        b[2] += dt
        b[1] += k2*(wind.y-vb)
        fill(255)
        circle(b[0], b[1], 10)
    vb += dt*ab
    ab = vb*k2
        
def mouseClicked():
            
def bombinha():
    time_b=0
    global B
    n = rd.randint(r, width - r)
    B.append([n, -r,time_b])
