import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, gravity=1.5):
        super().__init__()
        self.image = pygame.image.load('player_placeholder.png').convert_alpha()  # Placeholder for player sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.gravity = gravity
        self.velocity_y = 0
        self.is_jumping = False
        self.jump_height = -15  # Jump height value
        self.is_falling = False

    def update(self, platforms):
        self.handle_gravity()
        self.move()
        self.check_platform_collisions(platforms)
        self.check_if_fell_off_screen()

    def handle_gravity(self):
        """Apply gravity to the player."""
        if not self.is_jumping:
            self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

    def move(self):
        """Move the player based on key input."""
        keys = pygame.key.get_pressed()

        # Move left
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5

        # Move right
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        # Jump
        if keys[pygame.K_SPACE] and not self.is_jumping and not self.is_falling:
            self.velocity_y = self.jump_height
            self.is_jumping = True

    def check_platform_collisions(self, platforms):
        """Detect collision with platforms and adjust the player's position."""
        for platform in platforms:
            if pygame.sprite.collide_rect(self, platform) and self.velocity_y > 0:
                self.rect.y = platform.rect.top - self.rect.height
                self.velocity_y = 0
                self.is_jumping = False
                return

    def check_if_fell_off_screen(self):
        """Check if the player falls off the screen."""
        if self.rect.y > 600:  # Screen height threshold
            self.respawn()

    def respawn(self):
        """Respawn the player at the start of the level."""
        self.rect.x = 100  # Respawn x position
        self.rect.y = 100  # Respawn y position
        self.velocity_y = 0
        self.is_jumping = False
        self.is_falling = False
