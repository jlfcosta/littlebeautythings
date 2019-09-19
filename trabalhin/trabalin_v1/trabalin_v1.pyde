import random as rd

bolinha_raio = 20
bolinhax = 20
bolinhay = 20
multx = 1
multy = 1
vetorzin_azul = []
vetorzin_vermelho = []

# Variáveis constantes
coex = 4
coey = 10

def setup():
    size(1830, 910)
    background(0)
    
def draw():
    global bolinhax, bolinhay, multx, multy, bolinha_raio, coex, coey
    global vetorzin_azul, vetorzin_vermelho
    
    if bolinhax > (width - bolinha_raio): multx *= -1
    elif bolinhax < bolinha_raio: multx *= -1
    
    if bolinhay > (height - bolinha_raio): multy *= -1
    elif bolinhay < bolinha_raio: multy *= -1
    
    bolinhax += multx*coex
    bolinhay += multy*coey
    
    fill(0)
    circle(bolinhax - multx*coex, bolinhay - multy*coey, 2*bolinha_raio)
    
    fill(255)
    noStroke()
    circle(bolinhax, bolinhay, 2*bolinha_raio)
    
    if frameCount % 30 == 0:
        remix()
        
    for i in vetorzin_azul:
        if ((bolinhax - i[0])**2 + (bolinhay - i[1])**2)**0.5 <= 30:
            vetorzin_azul.remove(i)
            fill(0)
            noStroke()
            circle(i[0], i[1], bolinha_raio)
            multx *= 1.3
            multy *= 1.3
            
    for i in vetorzin_vermelho:
        if ((bolinhax - i[0])**2 + (bolinhay - i[1])**2)**0.5 <= 30:
            vetorzin_vermelho.remove(i)
            fill(0)
            noStroke()
            circle(i[0], i[1], bolinha_raio)
            multx *= 0.8
            multy *= 0.8
        
def remix():
    global vetorzin_azul, vetorzin_vermelho
    if rd.randint(0, 1) == 0:
        vetorzin_azul.append((rd.randint(bolinha_raio, width), rd.randint(bolinha_raio, height)))
        fill(0, 0, 300)
        noStroke()
        circle(vetorzin_azul[len(vetorzin_azul) - 1][0], vetorzin_azul[len(vetorzin_azul) - 1][1], bolinha_raio)
    else:
        vetorzin_vermelho.append((rd.randint(bolinha_raio, width), rd.randint(bolinha_raio, height)))
        fill(300, 0, 0)
        noStroke()
        circle(vetorzin_vermelho[len(vetorzin_vermelho) - 1][0], vetorzin_vermelho[len(vetorzin_vermelho) - 1][1], bolinha_raio)
