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
 
pygame.display.set_caption("Bouncing Balls")
done = False 
clock = pygame.time.Clock()
ball_list = []
ball = make_ball()
ball_list.append(ball)
 

class Ball(object)
  def __init__(self):
        self.x = 10 
        self.y = 10
        self.change_x = 10
        self.change_y = 10

def construct_ball():
ball = Ball()
  ball.x = 10
  ball.y = 10
 
    return ball


class paddle(object)
  def __init_(self):
    self.x = 15
    self.y = 20

def construct_paddle():
paddle = paddle()

    paddle.x = 10
    paddle.y = 15
 
    return paddle

  def movement(self, width, height):
    key = pygame.key.get_pressed()
    if key[pygame.K_DOWN]:
   self.y+ =1
    if key[pygame.K_UP]:

      if key[pygame.K_RIGHT]:

        if key[pygame.K_LEFT]:
    






#If the ball ever touches the rightmost wall of the screen the game loop should end completely. 
 
#resource used- http://programarcadegames.com/python_examples/f.php?file=bouncing_balls.py https://sites.google.com/site/thepythonpongtutorial/drawing-functions/drawing-functions