r = 20 # (variável)
bol_vec = PVector(0, 0)
speed_vec = PVector(0, 0)
time = 0
k = 0
resistance = 0
gravity = 0
bombinhas = []

def setup():
    global r, bol_vec
    
    size(1800, 900) # (variável).
    bol_vec.x = r
    bol_vec.y = height - r
    
def draw():
    global r, bol_vec, speed_vec, time, k, resistance, gravity, bombinhas
    background(127)
    time += 0.05
    
    bol_vec.x += time*speed_vec.x + 0.5*resistance*time*time
    bol_vec.y += time*speed_vec.y + 0.5*gravity*time*time
    
    if bol_vec.x > width - r or bol_vec.x < r or bol_vec.y > height - r:
        bol_vec = PVector(r, height - r)
        speed_vec = PVector(0, 0)
        k = float('%.2f' % randomGaussian())/5
        resistance = 0
        gravity = 0
        
    #if frameCount%100 == 0:
        
    textSize(30)
    fill(64)
    text(("<< " + str(k)) if k < 0 else ("        " + str(k) + " >>"), 450, 50)
    
    noStroke()
    fill(255)
    circle(bol_vec.x, bol_vec.y, 2*r)
    
def mouseClicked():
    global time, resistance, gravity, bol_vec, speed_vec
    
    time = 0
    gravity = 2*9.8
    speed_vec = (PVector(mouseX, mouseY) - bol_vec)/17
    speed_vec.x /= 3
    resistance = ventinho()
    
def ventinho():
    global k
    
    return k*speed_vec.x
