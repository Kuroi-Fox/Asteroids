import pygame
from circleshape import *
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
          
          super().__init__(x, y, radius)
    
    def draw(self, screen):
         pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
         self.position += (self.velocity * dt)
     
    def split(self):
         self.kill()
         if self.radius <= ASTEROID_MIN_RADIUS:
              return
         else:
              log_event("asteroid_split")
              new_radius =  self.radius - ASTEROID_MIN_RADIUS
              asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
              asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
              angle = random.uniform(20, 50)
              asteroid_one.velocity = self.velocity.rotate(angle) * 1.2
              asteroid_two.velocity = self.velocity.rotate(-angle) * 1.2
     
              



