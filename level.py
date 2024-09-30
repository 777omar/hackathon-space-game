from platformm import Platform
from part import Part

class Level:
    def __init__(self, level_number):
        self.level_number = level_number
        self.platforms = self.create_platforms()
        self.parts = Part.generate_parts(10, [p.rect for p in self.platforms])
        self.gravity = self.set_gravity()

    def create_platforms(self):
        platforms = []
        # Example platform placements; adjust as needed for each level
        if self.level_number == 1:  # Jupiter
            platforms.append(Platform(50, 500, 200, 20))
            platforms.append(Platform(300, 400, 200, 20))
            platforms.append(Platform(600, 300, 200, 20))
        # Add more platforms for other levels...

        return platforms

    def set_gravity(self):
        if self.level_number == 1:  # Jupiter
            return 1.5
        elif self.level_number == 2:  # Venus
            return 1.2
        elif self.level_number == 3:  # Mars
            return 1.0
        elif self.level_number == 4:  # Mercury
            return 0.8
        elif self.level_number == 5:  # The Moon
            return 0.5
