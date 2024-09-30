import pygame 

class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = min(0, target.rect.centerx - int(self.width / 2))
        x = max(-(self.width - self.width), x)
        y = min(0, target.rect.centery - int(self.height / 2))
        y = max(-(self.height - self.height), y)
        self.camera = pygame.Rect(x, y, self.width, self.height)
