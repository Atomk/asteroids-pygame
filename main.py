import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    numpass, numfail = pygame.init()
    print(f"Passed: {numpass}, failed: {numfail}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    delta_time = 0  # seconds
    FPS = 60

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    # Ensure that all new objects are automatically added to these groups upon creation.
    # This works because the Sprite constructor uses `containers` if available
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    asteroids_generator = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        updatable.update(delta_time)
        for entity in drawable:
            entity.draw(screen)

        pygame.display.flip()

        delta_time =  clock.tick(FPS) / 1000


if __name__ == "__main__":
    main()