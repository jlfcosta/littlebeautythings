v = PVector(3, 7)
p = PVector(20, 20)

def setup():
    size(1600, 800)
    
def draw():
    global v, p
    p = p.add(v)
    
    if p.x <= 20 or p.x >= width - 20: v.x = v.x*(-1)
    if p.y <= 20 or p.y >= height -20: v.y = v.y*(-1)
    
    background(0)
    noStroke()
    fill(255)
    circle(p.x, p.y, 40)
    
def mouseClicked():
    global v
    m = PVector(mouseX, mouseY)
    
    diretor = m.add((-1)*p)
    dir_mag = diretor.mag()
    diretor.x = diretor.x/dir_mag
    diretor.y = diretor.y/dir_mag
    diretor = diretor*v.mag()
    
    v = diretor
