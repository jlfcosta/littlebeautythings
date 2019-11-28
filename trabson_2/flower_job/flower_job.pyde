#parâmetros da curva
R = 200
R2 = 10
b = 1
multi=1
def linspace(start,stop,num=6400):
    res=[]
    i=start
    inc=(stop-start)/num
    for _ in range(num):
        res.append(i)
        i+=inc
    return res
if b%2==0:
    range_theta = linspace(0,2*PI)
elif b%2==1:
    range_theta = linspace(0,PI)
flowerx=[R*cos(b*i)*cos(i) for i in range_theta]
flowery=[R*cos(b*i)*sin(i) for i in range_theta]
theta=range_theta[flowery.index(max(flowery))]
mode = 0
#parâmetros do movimento
g = 980.0 #cm/s²
a = PVector(0,-g) # aceleração da gravidade
# if b%2==0:
#     theta=HALF_PI
# else:
#     theta=2*PI/b
#theta = HALF_PI
vt=0#PVector(0,0)
oldt=millis()/1000.0

v = PVector(-R*(cos(b*theta)*sin(theta)+b*sin(b*theta)*cos(theta)),R*(cos(b*theta)*cos(theta)-b*sin(b*theta)*sin(theta)))
def setup():
    size(500,500)
    
def draw():
    translate(width/2,height/2)
    #rotate(PI)
    scale(1,-1)
    global R,R2,b,g,a,theta,oldt,flowerx,flowery,v,vt,g,multi
    t=millis()/1000.0
    dt = t - oldt
    oldt = t
    
    #componente tangencial da aceleração proj_v(a)
    # if mode ==0:
    #     v=PVector(v.x,0)
    v = PVector(-R*(cos(b*theta)*sin(theta)+b*sin(b*theta)*cos(theta)),R*(cos(b*theta)*cos(theta)-b*sin(b*theta)*sin(theta)))
    at1 = v.mult(PVector(0,-g).dot(v)/v.magSq())
    at = at1.mag()*multi
    # atualização da posição
    theta += vt*dt/R
    #atualização da velocidade
    #vt.add(at.mult(dt))
    vt += at*dt
    #posição cartesiana
    pos = PVector(R*cos(theta)*cos(b*theta),R*sin(theta)*cos(b*theta))
    ff=PVector(0,0)
    PVector.cross(pos,at1,ff)
    if ff.z>0:
        multi=-1
    elif ff.z<0:
        multi=1
    background(255)
    
    for i in range(len(flowerx)-1):
        stroke(0)
        # line(width/2+flowerx[i], height/2-flowery[i], width/2+flowerx[i+1], height/2-flowery[i+1])
        # ellipse(x+width/2,height/2-y,R2,R2)
        line(flowerx[i], flowery[i],flowerx[i+1],flowery[i+1])
        #point(250+flowerx[i],250-flowery[i])
    ellipse(pos.x,pos.y,R2,R2)
    print(multi,ff)
    #rect(20,20,40,40)
def mouseClicked():
    global vt, mode
    mode = 1
    vt=40#PVector(+5,0)
