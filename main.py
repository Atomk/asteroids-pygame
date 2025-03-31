import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from text import Text

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
    shots = pygame.sprite.Group()
    # Ensure that all new objects are automatically added to these groups upon creation.
    # This works because the Sprite constructor uses `containers` if available
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    asteroids_generator = AsteroidField()
    score = 0

    text_score_label = Text("Score: ")
    text_score_label.rect.left = 50
    text_score_label.rect.top = 50

    text_score_val = Text(str(score))
    text_score_val.rect.left = text_score_label.rect.right + 10
    text_score_val.rect.top = text_score_label.rect.top

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        text_score_label.draw(screen)
        text_score_val.draw(screen)

        updatable.update(delta_time)
        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                print(f"Game over! Score: {score}")
                sys.exit()
            for shot in shots:
                if shot.is_colliding(asteroid):
                    #print(f"Destroyed asteroid, radius: {asteroid.radius}, points: {asteroid.get_points()}")
                    score += asteroid.get_points()
                    text_score_val.update_string(str(score))
                    shot.kill()
                    asteroid.split()
        for entity in drawable:
            entity.draw(screen)

        pygame.display.flip()

        delta_time =  clock.tick(FPS) / 1000


if __name__ == "__main__":
    main()