bolinha = 0
raio = 20 #
velocidade = PVector(0, 0)
gravidade = 0
ventin = 0
k = 0
tempo = 0

def setup():
    global bolinha, raio
    
    size(900, 450) #
    bolinha = PVector(raio, height - raio)
    
def draw():
    global bolinha, raio, velocidade, gravidade, ventin, k, tempo
    
    tempo += 0.05
    
    # Velocidade relativa = velocidade do vento - velocidade da bolinha
    # V_r = V_v - V_b ... (1)
    # V(n) = V(n-1) + at
    # F = -kV(n-1)
    # a = -kV(n-1)/m ... (2)
    # Aplicando (1) em (2),
    # a = -k(V_v - V_b(n-1))/m
    
    velocidade.x = velocidade.x + k*(ventin - velocidade.x)
    bolinha.x = bolinha.x + velocidade.x*0.05 + (k*(ventin - velocidade.x)*0.05**2)/2
    bolinha.y = height - raio + tempo*velocidade.y - gravidade*0.5*tempo**2
    
    if bolinha.x < raio or bolinha.x > width - raio or bolinha.y > height - raio:
        bolinha = PVector(raio, height - raio)
        gravidade = 0
        ventin = float('%.2f' % randomGaussian())
    
    background(127)
    noStroke()
    fill(255)
    circle(bolinha.x, bolinha.y, 2*raio)
    
def mouseClicked():
    global bolinha, velocidade, gravidade
    
    velocidade = (PVector(mouseX, mouseY) - bolinha)/17
    velocidade.x /= 3
    gravidade = 2*9.8
