import pygame
import random


class Part(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('part_placeholder.png').convert_alpha()  # Placeholder for part sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    @staticmethod
    def generate_parts(num_parts, platform_rects):
        parts = pygame.sprite.Group()
        for _ in range(num_parts):
            while True:
                x = random.randint(0, 800)  # Adjust as needed
                y = random.randint(0, 600)  # Adjust as needed
                if any(rect.collidepoint(x, y) for rect in platform_rects):
                    part = Part(x, y)
                    parts.add(part)
                    break
        return parts
