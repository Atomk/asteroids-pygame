import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        raise NotImplementedError("Child classes must override this method.")

    def update(self, delta_time):
        raise NotImplementedError("Child classes must override this method.")

    def draw_collider(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)

    def is_colliding(self, other):
        """Returns whether this object is overlapping with another CircleShape."""
        distance = self.position.distance_to(other.position)
        return distance <= self.radius + other.radius
