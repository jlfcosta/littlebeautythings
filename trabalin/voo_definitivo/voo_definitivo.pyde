ball = 0
r = 20 #
wind_speed = 0
ball_speed = PVector(0, 0)
gravity = 9.8 #
acceleration = PVector(0, gravity)
resistence = PVector(0, 0)
t = 0
bomb_list = []
bomb_acceleration = PVector(0, gravity)
bomb_r = 40 #
points = 0
count = 0
perdeu = 0

def setup():
    global ball, r
    size(1800, 900) #
    ball = PVector(r, height - r)
def draw():
    global ball, r, wind_speed, ball_speed, gravity, acceleration, resistence, t, bomb_list, bomb_acceleration, bomb_r, points, count, perdeu
    rho = 1 #
    coef_ball = 0.47
    A = [2*PI*r*r, 2*PI*bomb_r*bomb_r]
    
    background(127)
    delta_t = 0.1 #
    t += delta_t
    count += delta_t
    #ball.x = r + ball_speed.x*t
    ball.x += ball_speed.x*delta_t
    ball.y = height - r + ball_speed.y*t + 0.5*acceleration.y*t*t
    #ball.y += ball_speed.y*delta_t + 0.5*acceleration.y*delta_t*delta_t
    
    #ball_speed.x += acceleration.x*
    
    if ball.x < r or ball.x > width - r or ball.y > height - r:
        ball = PVector(r, height - r)
        ball_speed *= 0
        acceleration *= 0
        t = 0
    
    if frameCount%90 == 0: #
        bomb()
        
    if perdeu == 1:
        ball = PVector(-2*r, -2*r, r)
        textSize(125)
        fill(0)
        text('hehe, morreu', 30, height - 30)
        textSize(20)
        text('aperta "r", vai', 30, 750)
        
    textSize(32)
    fill(255)
    text('points: ' + str(int(points)), 10, 40)
    for i in bomb_list:
        i[2] += delta_t
        i[1] = -bomb_r + 0.5*bomb_acceleration.y*i[2]**2
        if ((ball.x - i[0])**2 + (ball.y - i[1])**2)**0.5 < r + bomb_r - 2*(points//5):
            bomb_list.remove(i)
            ball_speed *= 0
            t = 0
            points += 1
            count = 0
        if i[1] >= height + bomb_r:
            bomb_list.remove(i)
            perdeu = 1
        noStroke()
        fill(0)
        circle(i[0], i[1], 2*bomb_r - 4*(points//5))
    
    noStroke()
    fill(255) 
    circle(ball.x, ball.y, 2*r)
    
    if points%5 == 0 and points > 0 and count < 20*delta_t:
        background(0)
        textSize(200)
        fill(255)
        text('fazi ' + str(int(points//5 + 1)), 30, height - 30)
        
    if keyPressed:
        if key == 'r':
            perdeu = 0
            bomb_list = []
            ball = PVector(r, height - r)
            points = 0
        
def mouseClicked():
    global ball, ball_speed, acceleration, t
    if ball.y == height - r:
        ball_speed = (PVector(mouseX, mouseY) - ball)/3 #
        acceleration.y = gravity
        t = 0
def bomb():
    global bomb_list, bomb_r
    bomb_list.append([int(random(bomb_r, width - bomb_r)), -bomb_r, 0])
