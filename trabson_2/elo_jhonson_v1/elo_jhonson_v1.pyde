B = 0 # Posição da bolinha (inicial das duas).
B1 = 0 # Posição da bolinha 1.
B2 = 0 # Posição de bolinha 2.
aponta = 0 # Posição do lançamento.
g = 9.8 # Aceleração da gravidade.
dt = 0.2 # O intervalo de tempo.
mode = 0 # Modo de operação do aplicativo.

# Para o método de Euler:
teta = 0 # Ângulo inicial.
v = 0 # Velocidade inicial.

# Para o método de energia:
h = 0 # (modificar pelo setup()) Comprimento da cordinha.
phi0 = 0 # Ângulo inicial (referencial).
phi = 0 # Ângulo atual.
vel = 0 # Velocidade inicial.
multi = -1 # Multiplicador da orientação da velocidade.

def setup():
    global B, h
    size(900, 900)
    h = height/3
    B = PVector(0, h)

def draw():
    global B, B1, B2, g, v, dt, mode, h, teta, phi0, phi, vel, multi
    background(39, 255, 232)
    fill(255, 28, 194)
    stroke(43, 80, 255)
    strokeWeight(2)
    
    if mode == 1:
        at = g*cos(B1.heading())
        teta += v*dt/B1.mag()
        v += at*dt
        B1 = PVector(h*cos(teta), h*sin(teta))
        line(width/2, height/20, width/2 + B1.x, height/20 + B1.y)
        circle(width/2 + B1.x, height/20 + B1.y, height/30)
        
        if h*sin(phi0) >= h*sin(phi):
            multi *= -1
            print(1)
            print(B2.heading())
        else: vel = (2*g*h*(1 - sin(phi0))-2*g*h*(1 - sin(phi)))**0.5
        phi += multi*vel*dt/h
        
        B2 = PVector(h*cos(phi), h*sin(phi))
        line(width/2, 11*height/20, width/2 + B2.x, 11*height/20 + B2.y)
        circle(width/2 + B2.x, 11*height/20 + B2.y, height/30)
    
    
    line(4*width/9, height/20, 5*width/9, height/20)
    line(4*width/9, 11*height/20, 5*width/9, 11*height/20)
    if mode == 0:
        line(width/2, height/20, width/2 + B.x, height/20 + B.y)
        line(width/2, 11*height/20, width/2 + B.x, 11*height/20 + B.y)
        circle(width/2 + B.x, height/20 + B.y, height/30)
        circle(width/2 + B.x, 11*height/20 + B.y, height/30)
        
    textSize(height/45);
    text("\"Euler Method\", mais comumente conhecido por \"modo de fazer conta errada\".", width/30, 11*height/24)
    text("Utilizando conceitos de energia, assim fica: (olha ali em cima, olha que coisa linda).", width/30, 23*height/24)
    
def mousePressed():
    global B, aponta, mode
    aponta = PVector(mouseX - width/2, mouseY - height/20)
    B.rotate(aponta.heading() - B.heading())
    mode = 0

def mouseDragged():
    global B, aponta
    aponta = PVector(mouseX - width/2, mouseY - height/20)
    B.rotate(aponta.heading() - B.heading())
    
def mouseReleased():
    global B, B1, B2, teta, phi0, phi, v, vel, multi, mode
    teta = B.heading()
    phi0 = B.heading()
    if B.heading() > HALF_PI or B.heading() < -HALF_PI:
        phi = B.heading() - 0.00001
        multi = 1
    else:
        phi = B.heading() + 0.00001
        multi = -1
    v = 0
    vel = 0
    B1 = B
    B2 = B
    mode = 1
