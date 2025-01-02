import pygame
from player import *
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

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
        for dthing in drawable:
            dthing.draw(screen)
        #player.update(dt)
        #player.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()

