#parâmetros da curva
A = 200
b = 2
def linspace(start,stop,num=800):
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
flowerx=[A*cos(b*i)*cos(i) for i in range_theta]
flowery=[A*cos(b*i)*sin(i) for i in range_theta]

#parâmetros do movimento
g = 980.0
a = PVector(0,-g) # aceleração da gravidade
if b%2==1:
    theta=HALF_PI
else:
    theta=2*PI/b
vt=0
oldt=millis()/1000.0
v = PVector(-A*(cos(b*theta)*sin(theta)-b*sin(b*theta)*cos(theta)),A*(cos(b*theta)*cos(theta)-b*sin(b*theta)*sin(theta)))
def setup():
    size(500,500)
    
def draw():
    global A,b,g,a,vt,theta,oldt,flowerx,flowery
    t=millis()/1000.0
    dt = t - oldt
    oldt = t
    
    #componente tangencial da aceleração proj_v(a)
    at=
    background(255)
    
    for i in range(len(flowerx)-1):
        stroke(0)
        line(width/2+flowerx[i], height/2-flowery[i], width/2+flowerx[i+1], height/2-flowery[i+1])
        #point(250+flowerx[i],250-flowery[i])
