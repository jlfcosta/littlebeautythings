# Consideramos 1 pixel = 1 cm

ball = 0
m = 1 #
r = 15 #
wind_speed = PVector(0, 0) #
ball_speed = PVector(0, 0)
gravity = 9.8 #
acceleration = PVector(0, gravity)
resistence = PVector(0, 0)

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
    background(127)
    
def draw():
    global ball, m, r, wind_speed, ball_speed, gravity, acceleration, resistence, bomb_list, bomb_acceleration, bomb_r, points, count, perdeu
    
    rho = 1 #
    coef_ball = 0.47
    A = [2*PI*r*r/10000, 2*PI*bomb_r*bomb_r/10000]
    ball_k = rho*coef_ball*A[0]/2
    
    
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
        wind_speed.x = randomGaussian() #
        
    # textSize(32)
    # fill(255)
    # text('points: ' + str(int(points)), 10, 40)
    
    # if wind_speed.x > 0:
    #     textSize(32)
    #     fill(255)
    #     text('ventin:', 20, 70)
    #     if frameCount%40 < 19: text('   ' + str(float('%.2f' % wind_speed.x)) + ' > ', 10, 100)
    #     else: text('   ' + str(float('%.2f' % wind_speed.x)) + '  >', 10, 100)
    # elif wind_speed.x < 0:
    #     textSize(32)
    #     fill(255)
    #     text('ventin:', 20, 70)
    #     if frameCount%40 < 19: text(' < ' + str(float('%.2f' % wind_speed.x)) + '   ', 10, 100)
    #     else: text('<  ' + str(float('%.2f' % wind_speed.x)) + '   ', 10, 100)
    
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
        
def keyReleased():
    global ball, ball_speed, acceleration, t
    if key == ' ':
        if ball.y == height - r:
            ball_speed = (PVector(mouseX, mouseY) - ball)/3 #
            acceleration.y = gravity
