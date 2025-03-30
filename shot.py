import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def update(self, delta_time):
        self.position += self.velocity * delta_time

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)
