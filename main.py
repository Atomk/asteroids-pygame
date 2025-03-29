import pygame
from constants import *
from player import Player


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

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))
        player.update(delta_time)
        player.draw(screen)
        pygame.display.flip()

        delta_time =  clock.tick(FPS) / 1000


if __name__ == "__main__":
    main()