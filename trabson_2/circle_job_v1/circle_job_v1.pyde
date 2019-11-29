R = 150 #raio da trajetória
teta1 = HALF_PI #posição inicial
g = 980.0 #acelaração da gravidade em cm/s2
vt1 = 0 #velocidade incial simulação 1
vt2 = vt1 #velocidade incial simulação 2
teta2 = teta1 #posição inicial simulação 2
oldt = millis()/1000.0
wid = 800 #largura da tela
hei = 400 #altura da tela

def setup():
    size(wid,hei)
    
def draw():
    global oldt, teta1 , vt1, R, g,vt2,teta2
    
    t = millis()/1000.0
    dt = t - oldt
    oldt = t
    yi=R*sin(teta2)
    vi=vt2
    
    #aceleração tangencial (obtida projetando a gravidade na tangente ao círculo)
    at = -g*cos(teta1)
    #atualização da posição (delta_teta = v * delta_t /R)
    teta1 += vt1*dt/R
    teta2 += vt2*dt/R
    #atualização da velocidade
    vt1 += at*dt #euler
    vt2 = -(2*g*(yi-R*sin(teta2))+vi**2)**0.5 #energia
    #posição em coordenadas cartesianas
    x1 = R*cos(teta1)
    y1 = R*sin(teta1)
    x2 = R*cos(teta2)
    y2 = R*sin(teta2)

    #desenho
    background(225)
    fill(0)
    ellipse(wid/4,hei/2,2*R,2*R)
    fill(255,255,0)
    ellipse(x1+wid/4, hei/2-y1, 10, 10)
    fill(255,0,0)
    fill(0)
    ellipse(3*wid/4,hei/2,2*R,2*R)
    fill(255,0,0)
    ellipse(x2+3*wid/4, hei/2-y2, 10, 10)

def mouseClicked():
    global vt1,vt2
    vt1 = -10
    vt2 = -10
