import pygame

class UI:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('Arial', 24)

    def draw_oxygen_bar(self, oxygen_percentage):
        pygame.draw.rect(self.screen, (255, 0, 0), (10, 10, 200, 20))  # Background bar
        pygame.draw.rect(self.screen, (0, 255, 0), (10, 10, 2 * oxygen_percentage, 20))  # Current oxygen level

    def display_text(self, text, x, y):
        text_surface = self.font.render(text, True, (255, 255, 255))
        self.screen.blit(text_surface, (x, y))
