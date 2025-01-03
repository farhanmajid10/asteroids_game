from circleshape import CircleShape
from constants import *
import pygame
import random
class Asteroid(CircleShape):
    def __init__(self, x,y,radius):
        super().__init__(x,y,radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen,"white", self.position,self.radius, 2)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 1
        angle = random.uniform(20,50)
        left = self.velocity.rotate(angle)
        right = self.velocity.rotate(-angle)


        new_radius = self.radius - ASTEROID_MIN_RADIUS
        left_asteroid = Asteroid(self.position.x,self.position.y, new_radius)
        right_asteroid = Asteroid(self.position.x,self.position.y, new_radius)
        left_asteroid.velocity = left * 1.2
        right_asteroid.velocity = right * 1.2
        return 2
