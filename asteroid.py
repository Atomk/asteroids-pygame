import pygame
import random
import math
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS

class Asteroid(CircleShape):
    debug = False

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.vertices = self.generate_vertices()

    def generate_vertices(self):
        vertices = []
        angle = 0
        while angle < 360:
            direction = pygame.Vector2(
                math.sin(math.radians(angle)),
                math.cos(math.radians(angle)),
            )
            scale = self.radius * random.uniform(0.8, 1.05)
            vertices.append(self.position + direction * scale)
            angle += random.uniform(30, 45)
        return vertices

    def draw(self, screen):
        if self.debug:
            self.draw_collider(screen)
        pygame.draw.polygon(screen, "white", self.vertices, 2)

    def update(self, delta_time):
        offset = self.velocity * delta_time
        self.position += offset
        for vert in self.vertices:
            vert += offset

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        speed_multiplier = 1.2

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = self.velocity.rotate(random_angle) * speed_multiplier

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = self.velocity.rotate(-random_angle) * speed_multiplier

    def get_points(self):
        return  20 + ASTEROID_MAX_RADIUS - self.radius
