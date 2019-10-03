# Consideramos 1 pixel = 1 cm

ball = 0
m = 1 #
r = 20 #
wind_speed = PVector(0, 0) #
ball_speed = PVector(0, 0)
gravity = 9.8 #
acceleration = PVector(0, gravity)

bomb_list = []
bomb_acceleration = PVector(0, gravity)
bomb_r = 40 #
points = 0
count = 0
perdeu = 0

def setup():
    global ball, r
    
    size(900, 900) #
    ball = PVector(r, height - r)
    
def draw():
    global ball, m, r, wind_speed, ball_speed, gravity, acceleration, bomb_list, bomb_acceleration, bomb_r, points, count, perdeu
    
    rho = 1 #
    coef_ball = 0.47
    A = [2*PI*r*r/10000, 2*PI*bomb_r*bomb_r/10000]
    ball_k = rho*coef_ball*A[0]/2
    
    background(127)
    delta_t = 0.1 #
    count += delta_t
    
    ball_speed.x += acceleration.x*delta_t
    acceleration.x = ball_k*(wind_speed.x - ball_speed.x)/m
    ball_speed.y += acceleration.y*delta_t
    acceleration.y = ball_k*(wind_speed.y - ball_speed.y)/m + gravity
    ball.x += ball_speed.x*delta_t + 0.5*acceleration.x*delta_t*delta_t
    ball.y += ball_speed.y*delta_t + 0.5*acceleration.y*delta_t*delta_t
    
    if ball.x < r or ball.x > width - r or ball.y > height - r:
        ball = PVector(r, height - r)
        ball_speed *= 0
        acceleration *= 0
    
    if frameCount%100 == 0: #
        bomb()
    
    if perdeu == 1:
        ball = PVector(-2*r, -2*r, r)
        ball_speed *= 0
        acceleration *= 0
        textSize(125)
        fill(0)
        text('hehe, morreu', 30, height - 30)
        textSize(20)
        text('aperta "r", vai', 30, 750)
        
        if keyPressed:
            if key == 'r':
                perdeu = 0
                bomb_list = []
                ball = PVector(r, height - r)
                points = 0
    
    for i in bomb_list:
        i[2] += delta_t
        i[1] = -bomb_r + 0.5*bomb_acceleration.y*i[2]**2
        if ((ball.x - i[0])**2 + (ball.y - i[1])**2)**0.5 < r + bomb_r - 2*(points//5):
            bomb_list.remove(i)
            ball = PVector(r, height - r)
            ball_speed *= 0
            acceleration *= 0
            points += 1
            count = 0
            stage = 1 + points//5
            if stage%4 == 0:
                wind_speed.x = randomGaussian()
            else: wind_speed.x = 0
        if i[1] >= height + bomb_r:
            bomb_list.remove(i)
            perdeu = 1
        noStroke()
        fill(0)
        circle(i[0], i[1], 2*bomb_r - 4*(points//5))
        
    textSize(32)
    fill(255)
    text('points: ' + str(int(points)), 10, 40)
    
    if wind_speed.x > 0:
        textSize(32)
        fill(255)
        text('ventin:', 20, 70)
        if frameCount%40 < 19: text('   ' + str(float('%.2f' % wind_speed.x)) + ' > ', 10, 100)
        else: text('   ' + str(float('%.2f' % wind_speed.x)) + '  >', 10, 100)
    elif wind_speed.x < 0:
        textSize(32)
        fill(255)
        text('ventin:', 20, 70)
        if frameCount%40 < 19: text(' < ' + str(float('%.2f' % wind_speed.x)) + '   ', 10, 100)
        else: text('<  ' + str(float('%.2f' % wind_speed.x)) + '   ', 10, 100)
    
    noStroke()
    fill(255) 
    circle(ball.x, ball.y, 2*r)
    
    # (Estética braba) Caso a bolinha branca não estiver se mexendo, uma setinha surge nela.
    if acceleration.y == 0:
        z = PVector(mouseX - ball.x, mouseY - ball.y).normalize()
        j = PVector(mouseX - ball.x, mouseY - ball.y).normalize().rotate(0.7853981)
        h = PVector(mouseX - ball.x, mouseY - ball.y).normalize().rotate(5.4977871)
        z *= 9*r/5
        j *= r
        h *= r
        
        fill(255)
        triangle(ball.x + z.x, ball.y + z.y, ball.x + j.x, ball.y + j.y, ball.x + h.x, ball.y + h.y)
    
    if points%5 == 0 and points > 0 and count < 20*delta_t:
        background(0)
        textSize(200)
        fill(255)
        text('fazi ' + str(int(points//5 + 1)), 30, height - 30)

# def mouseClicked():
#     global ball, ball_speed, acceleration, t
#     if ball.y == height - r:
#         ball_speed = (PVector(mouseX, mouseY) - ball)/3 #
#         acceleration.y = gravity

def bomb():
    global bomb_list, bomb_r
    bomb_list.append([int(random(bomb_r, width - bomb_r)), -bomb_r, 0])
    
def keyReleased():
    global ball, ball_speed, acceleration, t
    if key == ' ':
        if ball.y == height - r:
            ball_speed = (PVector(mouseX, mouseY) - ball)/3 #
            acceleration.y = gravity
