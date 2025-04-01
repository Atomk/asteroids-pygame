import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 180
        self.shoot_cooldown = 0

    def triangle(self) -> list[pygame.Vector2]:
        """Generates a list of three vertices."""
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        # TODO do not regenerate the list every frame, only when needed. COuld also use a tuple
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += direction * PLAYER_SPEED * dt

    def update(self, delta_time):
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= delta_time

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-delta_time)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(delta_time)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(delta_time)

        if keys[pygame.K_SPACE]:
            if self.shoot_cooldown <= 0:
                self.shoot()

    def shoot(self):
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
