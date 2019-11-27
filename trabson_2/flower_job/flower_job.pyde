#parâmetros da curva
a = 200
b = 3
def linspace(start,stop,num=800):
    res=[]
    i=start
    inc=(stop-start)/num
    for _ in range(num):
        res.append(i)
        i+=inc
    return res
range_theta = linspace(0,2*PI)
flowerx=[a*cos(b*theta)*cos(theta) for theta in range_theta]
flowery=[a*cos(b*theta)*sin(theta) for theta in range_theta]

def setup():
    size(500,500)
def draw():
    background(255)
    
    for i in range(len(flowerx)-1):
        stroke(0)
        line(width/2+flowerx[i], height/2-flowery[i], width/2+flowerx[i+1], height/2-flowery[i+1])
        #point(250+flowerx[i],250-flowery[i])
