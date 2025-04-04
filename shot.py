import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.lifetime = 0

    def update(self, delta_time):
        # Lifeitime prevents infinite wraparound
        self.lifetime += delta_time
        if self.lifetime > SHOT_LIFETIME:
            self.kill()
            return

        self.position += self.velocity * delta_time
        # wraparound x
        if self.position.x < -self.radius:
            self.position.x = SCREEN_WIDTH + self.radius
        elif self.position.x > SCREEN_WIDTH + self.radius:
            self.position.x = -self.radius
        # wraparound y
        if self.position.y < -self.radius:
            self.position.y = SCREEN_HEIGHT + self.radius
        elif self.position.y > SCREEN_HEIGHT + self.radius:
            self.position.y = -self.radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 1)
