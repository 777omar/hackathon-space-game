import pygame

class Sounds:
    def __init__(self):
        self.jump_sound = None
        self.collect_sound = None
        self.repair_sound = None
        self.finish_sound = None
        self.die_sound = None

    def load_sounds(self):
        self.jump_sound = pygame.mixer.Sound('jump.wav')
        self.collect_sound = pygame.mixer.Sound('collect.wav')
        self.repair_sound = pygame.mixer.Sound('repair.wav')
        self.finish_sound = pygame.mixer.Sound('finish.wav')
        self.die_sound = pygame.mixer.Sound('die.wav')

    def play_jump_sound(self):
        self.jump_sound.play()

    def play_collect_sound(self):
        self.collect_sound.play()

    def play_repair_sound(self):
        self.repair_sound.play()

    def play_finish_sound(self):
        self.finish_sound.play()

    def play_die_sound(self):
        self.die_sound.play()
