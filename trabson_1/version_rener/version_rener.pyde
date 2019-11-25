#Modelando lançamento do projétil
import random as rd
r = 0.30

v0 = PVector(0,0)
p0=PVector(r,r)
modv0=20
B=[]
a = PVector(0,0)
#
t0 = millis()
oldt = t0/1000.0
diretor=PVector(0,0)
mode=0 #parado - mode 1 em movimento
fase = 1
crash = 1
incr=1 # velocidade
tb0=millis()/1000.0 
def bombinha():
        global B
        B.append([rd.randint(30,width-30),0])
        global tb0
        tb0 = millis()/1000.0
def setup():
    size(1000,550)
def draw():
    global r,v0,t0,oldt,modv0,a,p0,mode,diretor,fase,crash,incr
    
    if mousePressed:
        mode = 1
        global oldt, t0
        t0 = millis()
        oldt = t0/1000.0
        diretor = PVector(mouseX-p0.x, height-mouseY-p0.y).normalize()
    if frameCount%int(200/fase) ==0:
        bombinha()
    
    if mode ==0: 
        
        pyx_p=p0.copy()
        pyx_p.x=100*p0.x
        pyx_p.y=height-100*p0.y
    elif mode == 1:   
        t = (millis()-t0)/1000.0  
        global diretor
        diretor.y=1*diretor.y
        v= diretor*modv0
        a.y=-9.8
        p=p0.copy()
        #p.x=p0.x+v.x*t
        p=p0+v*t+a*t*t
        pyx_p=p.copy()
        pyx_p.x=p.x*100
        pyx_p.y=height - 100*p.y
        print('posicao: ',pyx_p,t)
        
        oldt = t       
        
    if pyx_p.y + r*100 > height: #or pyp_p.x < r*100 or p.x > width:
        mode = 0
   
    
        
    background(23,22,64)
    textSize(32)
    fill(255, 50, 50);
    text("Fase "+str(fase), width-120 , 60);
    
    
    for i in B:
        global r,tb0,fase,incr
        tbn=millis()/1000.0
        rmini=10
        
        fill(242,184,162)
        noStroke
        circle(float(i[0]),float(i[1]),rmini)
        i[1] += incr#incr*(tbn-tb0)+((9.8)/2)*(tbn-tb0)**2
        if ((pyx_p.x-i[0])**2+(pyx_p.y-i[1])**2)**0.5<=rmini+r*100:
            mode=1
            
            crash += 1
            B.remove(i)
            if crash%6==0:
                fase += 1
                incr += 0.5
    # c1 = (3,3,13)
    # c2 = (50,32,89)
    # amt = 0.5
    # lerpColor(c1, c2, amt)
    fill(92,79,3)
    noStroke
    circle(pyx_p.x,pyx_p.y,2*100*r)
    
    
