import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from text import Text, LabeledValue

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
    game_paused = False
    asteroids_generator = AsteroidField()
    score = 0

    TEXT_COLOR = "gray"
    text_score = LabeledValue("Score: ", "0", TEXT_COLOR)
    text_score.rect.top = 40
    text_score.rect.left = 40

    asteroids_killed = 0
    text_asteroids_killed = LabeledValue("Asteroids: ", "0", TEXT_COLOR)
    text_asteroids_killed.rect.top = 80
    text_asteroids_killed.rect.left = 40

    pause_overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    pause_overlay.set_alpha(128)
    pause_overlay.fill("black")

    text_paused = Text("PAUSED", TEXT_COLOR)
    text_paused.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
                    game_paused = not game_paused
                elif event.key == pygame.K_F1:
                    Asteroid.debug = not Asteroid.debug
                    Player.debug = not Player.debug

        screen.fill((0, 0, 0))

        if not game_paused:
            updatable.update(delta_time)
            for asteroid in asteroids:
                if not asteroid.outside_allowed_area():
                    asteroid.kill()
                    continue
                if player.is_colliding(asteroid):
                    print(f"Game over! Score: {score}")
                    sys.exit()
                for shot in shots:
                    if shot.is_colliding(asteroid):
                        #print(f"Destroyed asteroid, radius: {asteroid.radius}, points: {asteroid.get_points()}")
                        score += asteroid.get_points()
                        text_score.update_suffix(str(score))
                        shot.kill()
                        asteroid.split()
                        asteroids_killed += 1
                        text_asteroids_killed.update_suffix(str(asteroids_killed))

        for entity in drawable:
            entity.draw(screen)

        text_score.draw(screen)
        text_asteroids_killed.draw(screen)

        if game_paused:
            screen.blit(pause_overlay, (0, 0))
            text_paused.draw(screen)

        pygame.display.flip()

        delta_time =  clock.tick(FPS) / 1000


if __name__ == "__main__":
    main()