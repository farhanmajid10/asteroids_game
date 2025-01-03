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
    score = 0
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
                    thing.kill()
                    if obj.split() == 1:
                        score += 3
                    else:
                        score += 1

        font = pygame.font.SysFont("Arial" , 24) #takes font from system.
        txtsurf = font.render(f"Score : {score}", True, "white") #Parameters: text, anti-aliasing for better text edges, color. Returns surface_object containing rendered text.
        screen.blit(txtsurf, (txtsurf.get_width() // 2, txtsurf.get_height() // 2))#get_width and get_height get the width in pixels. The blit function draws the text into the screen. Parameters: 

        pygame.display.flip()


if __name__ == "__main__":
    main()

