import pygame

# in case the global init was not performed yet
pygame.font.init()

default_font = pygame.font.get_default_font()
font = pygame.font.Font(default_font, 32)
#font = pygame.font.SysFont("Arial", 32)

class Text:
    def __init__(self, string: str, color="white"):
        self.color = color
        self.update_string(string)
        self.rect = self.texture.get_rect()

    def update_string(self, string: str):
        self.texture = font.render(string, True, self.color)

    def draw(self, screen: pygame.Surface):
        screen.blit(self.texture, self.rect)
