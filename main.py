#one player pong game
#Paddle, Ball, and 3 Walls. 
#move up and down 
#100 pixels in height, and 15 pixels in width
#ball and paddle should both properly collide as well as the ball and 3 walls to its left
#ball ever touches the rightmost wall of the screen the game loop should end completely
import pygame

def main():
  pygame.init()
  screen_width = 15
  screen_height = 100
  ball_size = 25 
  screen = pygame.time.Clock()
class Ball(object):
  def __init__(self):
        self.x = 10 
        self.y = 10
        self.change_x = 10
        self.change_y = 10
        self.size = 20
        self.colour = (0, 0, 255)
        self.thickness = 1
        
        def construct_ball():
          ball.x = 10
          ball.y = 10
        return ball
  def movement(self, width, height):
      key = pygame.key.get_pressed()
      if key[pygame.K_DOWN]:
  
        if key[pygame.K_UP]:

          if key[pygame.K_RIGHT]:

            if key[pygame.K_LEFT]:
              while:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit():
        ball = ball.move(speed)
        if ball.left < 0 or ball.right > width:
            speed[0] = -speed[0]
        if ball.top < 0 or ball.bottom > height:
            speed[1] = -speed[1] 

  def display(self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size, self.thickness)

class Paddle(object):
  def __init_(self):
    self.x = 15
    self.y = 20

def construct_paddle():

    paddle.x = 10
    paddle.y = 15
 
    return paddle
  if event.type == KEYDOWN:
                if event.key == K_UP:
                    player_paddle.direction = -1
                elif event.key == K_DOWN:
                    player_paddle.direction = 1
            if event.type == KEYUP:
                if event.key == K_UP and player_paddle.direction == -1:
                    player_paddle.direction = 0
                elif event.key == K_DOWN and player_paddle.direction == 1:
                    player_paddle.direction = 0

def bounce(self,screen_width,screen_height):
  self.x += self.x_velocity 
  self.y += self.y_velocity
if (self.y<= 0)=1
  self.y_velocity = 1
  if (self.y>= screen_height-50):
  self.y_velocity = -1
  if (self.x<=0):
    self.x_velocity =1 
    if (self.x_velocity>= screen_width-50):
      self.x_velocity= -1 

#If the ball ever touches the rightmost wall of the screen the game loop should end completely. 
  running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         pygame.quit()
                

#resource used- http://programarcadegames.com/python_examples/f.php?file=bouncing_balls.py https://sites.google.com/site/thepythonpongtutorial/drawing-functions/drawing-functions
#http://programarcadegames.com/python_examples/f.php?file=pong.py
#https://codereview.stackexchange.com/questions/144868/1-player-pong-with-ai