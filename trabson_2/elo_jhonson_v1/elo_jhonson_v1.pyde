B = 0 # Posição da bolinha (inicial das duas).
B1 = 0 # Posição da bolinha 1.
B2 = 0 # Posição de bolinha 2.
aponta = 0 # Posição do lançamento.
teta = 0 # Ângulo inicial.
g = 9.8 # Aceleração da gravidade.
v = 0.0 # Velocidade inicial.
dt = 0.1 # O intervalo de tempo.
mode = 0 # Modo de operação do aplicativo.

# Para o método de energia:
h = 0 # (modificar pelo setup()) Comprimento da cordinha.
phi0 = 0 # Ângulo inicial.
phi = 0 
vel = 0 # Velocidade inicial.
multi = -1 # Multiplicador da orientação da velocidade.

def setup():
    global B, h
    size(900, 900)
    h = height/3
    B = PVector(0, h)

def draw():
    global B, B1, B2, teta, g, v, dt, mode, h, phi0, phi, vel, multi
    background(192)
    
    if mode == 1:
        at = g*cos(B1.heading())
        teta += v*dt/B1.mag()
        v += at*dt
        B1 = PVector(h*cos(teta), h*sin(teta))
        line(width/2, 0, width/2 + B1.x, B1.y)
        circle(width/2 + B1.x, B1.y, 30)
        
        if 2*g*h*(1 - sin(phi0))-2*g*h*(1 - sin(phi)) <= 0:
            multi *= -1
            print(1)
        else: vel = (2*g*h*(1 - sin(phi0))-2*g*h*(1 - sin(phi)))**0.5
        phi += multi*vel*dt/h
        
        B2 = PVector(h*cos(phi), h*sin(phi))
        line(width/2, height/2, width/2 + B2.x, height/2 + B2.y)
        circle(width/2 + B2.x, height/2 + B2.y, 30)
    
    line(4*width/9, 0, 5*width/9, 0)
    line(4*width/9, height/2, 5*width/9, height/2)
    if mode == 0:
        line(width/2, 0, width/2 + B.x, B.y)
        line(width/2, height/2, width/2 + B.x, height/2 + B.y)
        circle(width/2 + B.x, B.y, 30)
        circle(width/2 + B.x, height/2 + B.y, 30)
    
def mousePressed():
    global B, aponta, mode
    aponta = PVector(mouseX - width/2, mouseY)
    B.rotate(aponta.heading() - B.heading())
    mode = 0

def mouseDragged():
    global B, aponta
    aponta = PVector(mouseX - width/2, mouseY)
    B.rotate(aponta.heading() - B.heading())
    
def mouseReleased():
    global B, B1, B2, teta, v, mode, phi, phi0, vel, multi
    teta = B.heading()
    if B.heading() < 90:
        phi = B.heading() + 0.00001
    else:
        phi = B.heading() - 0.00001
        multi *= -1
    phi0 = B.heading()
    v = 0
    vel = 0
    mode = 1
    B1 = B
    B2 = B
