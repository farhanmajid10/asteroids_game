import pygame
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()

    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids,updatable,drawable)
    Shot.containers = (updatable, drawable, shots)
    AsteroidField.containers = (updatable)
    AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(x,y)

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60)/1000
        screen.fill("black")
        
        for thing in updatable:
            thing.update(dt)
        
        for thing in asteroids:
            if player.collision(thing):
                print("Game Over!")
                return
            
        for dthing in drawable:
            dthing.draw(screen)
        for obj in asteroids:
            for thing in shots:
                if thing.collision(obj):
                    obj.kill()
                    thing.kill()
        pygame.display.flip()


if __name__ == "__main__":
    main()

