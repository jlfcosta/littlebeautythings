bolinhas = 4 # Quantidade de bolinhas.
lig_jhonson = [] # Lista das coordenadas dos ligamentos.
blist = [] # Lista das coordenadas das bolinhas.
h = 0 # (modificar pelo setup()) Comprimento da cordinha.
g = 9.8 # Aceleração da gravidade.
dt = 0.2 # Intervalo de tempo.
peixe = 0 # Um marcador usado para pescar as bolinhas.
#vizin = [] # Lista de bolinhas que são erguidas.
mode = 0 # Modo de operação do aplicativo.
aponta = 0

# Para o Método de Euler:
blist1 = []
veloci1 = [0]*bolinhas
teta = 0 # Ângulo inicial.

# Para o método da energia:
blist2 = []
veloci2 = [0]*bolinhas
phi0 = []
phi = [0]*bolinhas
multi = -1

def setup():
    global bolinhas, lig_jhonson, blist, h
    size(900, 900)
    h = 2*height/7  #  <<<
    for i in range(bolinhas):
        blist.append(PVector(0, h))
        lig_jhonson.append([2*width/7 + (i+1)*3*width/(7*(1 + bolinhas)), 
                            height/20])
    
def draw():
    global bolinhas, blist, blist1, blist2, veloci1, veloci2, lig_jhonson
    global aponta, h, g, mode, dt, multi
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
        # Colisões:
        for i in range(bolinhas - 1):
            if blist1[i].heading() - blist1[i+1].heading() <= -0.0001:
                blist1[i] = PVector(0, h)
                blist1[i+1] = PVector(0, h)
                opabomdia = veloci1[i+1]
                veloci1[i+1] = veloci1[i]
                veloci1[i] = opabomdia
            if blist2[i].heading() - blist2[i+1].heading() <= -0.0001:
            #if blist2[i+1][0] - blist2[i][0] < 3*width/(7*(1 + bolinhas)):
                blist2[i] = PVector(0, h)
                blist2[i+1] = PVector(0, h)
                opabomdia = phi0[i+1]
                phi0[i+1] = phi0[i]
                phi0[i] = opabomdia
                phi[i] = phi0[i+1]
                phi[i+1] = phi0[i]
                # opabomdia = veloci2[i+1]
                # veloci2[i+1] = veloci2[i]
                # veloci2[i] = opabomdia
                
        # Parte do Método de Euler:
        for i in range(bolinhas):
            at = g*cos(blist1[i].heading()) if blist1[i].heading() < -0.0001 or blist1[i].heading() > 0.0001 else 0
            blist1[i].rotate(veloci1[i]*dt/h)
            veloci1[i] += at*dt
            circle(blist1[i][0]+(2*width/7)+(i+1)*3*width/(7*(1+bolinhas)), 
                   blist1[i][1] + height/20, 3*width/(7*(1 + bolinhas)))
            line(lig_jhonson[i][0], lig_jhonson[i][1], 
                 blist1[i][0]+(2*width/7)+(i+1)*3*width/(7*(1+bolinhas)), 
                 blist1[i][1] + height/20)
            
        # Parte da energia:
        for i in range(bolinhas):
            if sin(phi0[i]) >= sin(phi[i]):
                multi *= -1
            else: veloci2[i] = (2*g*h*(sin(phi[i]) - sin(phi0[i])))**0.5
            blist2[i].rotate(multi*veloci2[i]*dt/h)
            # if veloci2[i] != 0:
            #     if sin(phi0) >= sin(phi):
            #         multi *= -1
            #     else: veloci2[i] = (2*g*h*(sin(phi) - sin(phi0)))**0.5
            # blist2[i].rotate(multi*veloci2[i]*dt/h)
            circle(blist2[i][0] + 2*width/7+(i+1)*3*width/(7*(1 + bolinhas)), 
                   blist2[i][1] + height/2 + height/20, 
                   3*width/(7*(1 + bolinhas)))
            line(lig_jhonson[i][0], lig_jhonson[i][1] + height/2, 
                 blist2[i][0] + 2*width/7 + (i+1)*3*width/(7*(1 + bolinhas)), 
                 blist2[i][1] + height/2 + height/20)
    
def mousePressed():
    global bolinhas, blist, lig_jhonson, h, peixe, vizin, mode, aponta
    global blist1, blist2
    mode = 0
    blist = []
    blist1 = []
    blist2 = []
    veloci1 = [0]*bolinhas
    veloci2 = [0]*bolinhas
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
    global mode, blist, blist1, blist2, bolinhas, phi0, phi, aponta, multi
    mode = 1
    # blist1 = []
    # blist2 = []
    for i in range(len(blist)):
        blist1.append(blist[i])
        blist2.append(blist[i])
    # blist1 = blist
    # blist2 = blist
    veloci1 = [0]*bolinhas
    veloci2 = [0]*bolinhas
    phi0 = [h*sin(blist2[i].heading()) for i in range(bolinhas)]
    if aponta.heading() > HALF_PI:
        for i in range(bolinhas):
            phi[i] = phi0[i] + 0.00001 if phi0[i] != HALF_PI else phi0[i]
        multi = 1
    else:
        for i in range(bolinhas):
            phi[i] = phi0[i] - 0.00001 if phi0[i] != HALF_PI else phi0[i]
        multi = -1
