import pygame

# in case the global init was not performed yet
pygame.font.init()

default_font = pygame.font.get_default_font()
font = pygame.font.Font(default_font, 28)
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


class LabeledValue(Text):
    def __init__(self, string: str, default_suffix: str, color="white"):
        super().__init__(string, color)
        self.prefix = string
        self.update_suffix(default_suffix)

    def update_string(self, string: str):
        self.prefix = string
        super().update_string(string)

    def update_suffix(self, suffix: str):
        self.texture = font.render(self.prefix + suffix, True, self.color)
