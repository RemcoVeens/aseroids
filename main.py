import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
import constants
from player import Player
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    astroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (astroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    x = constants.SCREEN_WIDTH // 2
    y = constants.SCREEN_HEIGHT // 2
    player = Player(x,y)
    AsteroidField()

    while True:
        screen.fill(color="black")
        updatable.update(dt)
        for stone in astroids:
            if player.coliding(stone):
                print("Game over!")
                return
            for pew in shots:
                if pew.coliding(stone):
                    stone.split()
                    pew.kill()



        for d in drawable:
            d.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) /1000



if __name__ == "__main__":
    main()
