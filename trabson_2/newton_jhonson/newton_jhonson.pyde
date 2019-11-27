bolinhas = 5 # Quantidade de bolinhas.
lig_jhonson = [] # Lista das coordenadas dos ligamentos.
blist = [] # Lista das coordenadas das bolinhas.
h = 0 # (modificar pelo setup()) Comprimento da cordinha.
peixe = 0 # Um marcador usado para pescar as bolinhas.
vizin = [] # Lista de bolinhas que são erguidas.
mode = 0 # Modo de operação do aplicativo.
aponta = 0

# Para o Método de Euler:
blist1 = []

# Para o método da energia:
blist2 = []

def setup():
    global bolinhas, lig_jhonson, blist, h
    size(900, 900)
    h = 2*height/7  #  <<<
    for i in range(bolinhas):
        blist.append(PVector(0, h))
        lig_jhonson.append([2*width/7 + (i+1)*3*width/(7*(1 + bolinhas)), 
                            height/20])
    
def draw():
    global bolinhas, blist, blist1, blist2, lig_jhonson, h, mode
    background(191)
    strokeWeight(2)
    line(2*width/7, height/20, 5*width/7, height/20)
    line(2*width/7, 11*height/20, 5*width/7, 11*height/20)
    if mode == 0:
        for i in range(bolinhas):
            circle(blist[i][0] + 2*width/7 + (i+1)*3*width/(7*(1 + bolinhas)), 
                   blist[i][1] + height/20, 3*width/(7*(1 + bolinhas)))
            circle(blist[i][0] + 2*width/7 + (i+1)*3*width/(7*(1 + bolinhas)), 
                   blist[i][1] + height/2 + height/20, 
                   3*width/(7*(1 + bolinhas)))
            line(lig_jhonson[i][0], lig_jhonson[i][1], 
                blist[i][0] + 2*width/7 + (i+1)*3*width/(7*(1 + bolinhas)), 
                blist[i][1] + height/20)
            line(lig_jhonson[i][0], lig_jhonson[i][1] + height/2, 
                blist[i][0] + 2*width/7 + (i+1)*3*width/(7*(1 + bolinhas)), 
                blist[i][1] + height/2 + height/20)
    else:
        # Parte do Método de Euler:
        x = 0
        
    
def mousePressed():
    global bolinhas, blist, lig_jhonson, h, peixe, vizin, mode, aponta
    mode = 0
    blist = []
    for i in range(bolinhas):
        blist.append(PVector(0, h))
    for i in range(bolinhas):
        if mouseX > 2*width/7 + (i+0.5)*3*width/(7*(1 + bolinhas)) and mouseX < 2*width/7 + (i+1.5)*3*width/(7*(1 + bolinhas)):
            peixe = i
            print(peixe)
            break
    else:
        aponta = PVector(mouseX - lig_jhonson[peixe][0], 
                         mouseY - lig_jhonson[peixe][1])
        if aponta.heading() > HALF_PI or aponta.heading() < -HALF_PI:
            for j in range(peixe + 1):
                blist[j].rotate(aponta.heading() - blist[j].heading())
        else:
            for j in range(peixe, len(blist)):
                blist[j].rotate(aponta.heading() - blist[j].heading())
        
def mouseDragged():
    global aponta, blist, lig_jhonson, peixe
    aponta = PVector(mouseX - lig_jhonson[peixe][0], 
                     mouseY - lig_jhonson[peixe][1])
    if aponta.heading() > HALF_PI or aponta.heading() < -HALF_PI:
        for j in range(peixe + 1):
            blist[j].rotate(aponta.heading() - blist[j].heading())
    else:
        for j in range(peixe, len(blist)):
            blist[j].rotate(aponta.heading() - blist[j].heading())
    
def mouseReleased():
    global mode, blist, blist1, blist2
    mode = 1
    blist1 = blist
    blist2 = blist
