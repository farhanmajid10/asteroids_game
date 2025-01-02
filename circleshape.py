import pygame

#Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self,x,y,radius):
        #we will be using this later
        if hasattr(self,"containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius

    def draw(self, screen):
        pass
    
    def update(self, dt):
        pass    

    def collision(self, other):
        temp = pygame.Vector2.distance_to(self.position,other.position)
        if(temp <= self.radius + other.radius):
            return True
        else:
            return False