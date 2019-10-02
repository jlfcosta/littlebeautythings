import random as rd

# Declarando as variáveis: t = tempo, p = posição, v = velocidade, a = aceleração (gravidade):
t = 0
r= 20
p=PVector(0,0)
v = PVector(0, 0)
a = PVector(0, 0)
p0 = p.copy()
Vv=0
k=(r/100)*0.47*0.5
h=1/60

# B é a lista das coordenadas das bolinhas que estão caindo:
B = []

def setup():
    global p,p0
    size(900, 500)
    p = PVector(r, height-r)
    p0 = PVector(r, height-r)
def draw():
    global t, p, v, a, B ,p0,k,h

    t += 0.03
    # Atualização do vetor posição:
    p.add(v*t)
    p.y += 0.5*a.y*t*t
    v1 = v.x
    v2 = v1 +(1/60)*a.x
    a2 = k*v2
    
    v.x=v2
    a.x=a2
    
    # Reinicialização das variáveis caso a bolinha branca encontre um dos limites:
    if p.y >= height-r or p.x <= r or p.x >= width-r:
        t = 0
        p = p0
        v *= 0
        a *= 0
    
    # Desenho:
    background(160)
    noStroke()
    fill(255)
    circle(p.x, p.y, 50)
    
    # (Estética braba) Caso a bolinha branca não estiver se mexendo, uma setinha surge nela.
    if a.y == 0:
        m = PVector(mouseX - p.x, mouseY - p.y).normalize()
        j = PVector(mouseX - p.x, mouseY - p.y).normalize().rotate(0.7853981)
        k = PVector(mouseX - p.x, mouseY - p.y).normalize().rotate(5.4977871)
        m *= 45
        j *= 20
        k *= 20
        
        fill(255)
        triangle(p.x + m.x, p.y + m.y, p.x + j.x, p.y + j.y, p.x + k.x, p.y + k.y)
    
    if frameCount%170 == 50:
        bombinha() # Função de construção das bolinhas pretas.
    
    for i in B:
        i[1] += 1
        fill(0)
        circle(i[0], i[1], 10)
        
        # Reinicialização das variáveis caso haja interseção:
        if ((p.x - i[0])**2 + (p.y - i[1])**2)**0.5 <= 30:
            t = 0
            p = p0
            v *= 0
            a *= 0
            
            B.remove(i)
            
        # (Melhor parte do programa):
        if i[1] >= height:
            background(160)
            textSize(120)
            text("hehe, morreu", 10, 450)
                                    
    # Pequena historinha:
    # if frameCount <= 1000:
    #     textSize(20)
    #     fill(255)
    #     text("you,", 480, 680)
    #     text("after buying a missile launcher,", 480, 710)
    #     text("may protect yourself...", 480, 740)
    #     text("FROM OTHERS MISSILE LAUNCHERS!!!", 480, 770)
    #     text(":D", 480, 800)
            
def mouseClicked(): # Atualiza as variáveis com o clique do mouse:
    global t, p, v, a, k, Vv
    if a.y == 0:
        t = 0
        v = PVector(mouseX - p.x, mouseY - p.y).normalize()*14
        v.x = Vv-v.x
        a.x = k*(Vv-v.x)
        a.y = 9.8
        
def bombinha():
    global B
    n = rd.randint(5, width - 4)
    B.append([n, -5])
