import pygame
import sys
from astronaut import Player
from platformm import Platform
from part import Part
from level import Level
from camera import Camera
from ui import UI
from leaderboard import Leaderboard
from sounds import Sounds

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Astronaut Adventure")
    clock = pygame.time.Clock()

    # Initialize sound
    sounds = Sounds()
    sounds.load_sounds()

    # Initialize UI
    ui = UI(screen)

    # Initialize leaderboard
    leaderboard = Leaderboard('leaderboard.db')
    leaderboard.setup_leaderboard()

    # Game variables
    current_level_index = 0
    player_name = input("Enter your name for the leaderboard: ")
    player_score = 0

    # Main game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Level management
        level = Level(current_level_index + 1)
        player = Player(100, 500, gravity=level.gravity)  # Starting position
        all_sprites = pygame.sprite.Group()
        all_sprites.add(player)
        all_sprites.add(*level.platforms)
        all_sprites.add(*level.parts)

        # Game loop for the level
        start_ticks = pygame.time.get_ticks()  # Timer for level completion
        oxygen_percentage = 100

        while True:
            screen.fill((0, 0, 0))  # Clear screen

            # Check time
            seconds = (pygame.time.get_ticks() - start_ticks) / 1000
            if seconds > 180:  # 3 minutes for each level
                print("Time's up!")
                break

            # Decrease oxygen gradually
            oxygen_percentage = max(0, oxygen_percentage - (1 / 180 * FPS))
            if oxygen_percentage == 0:
                print("You ran out of oxygen!")
                break

            # Update player and sprites
            all_sprites.update(level.platforms)
            camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
            camera.update(player)

            # Draw all sprites
            for sprite in all_sprites:
                screen.blit(sprite.image, camera.apply(sprite))

            # Draw UI elements
            ui.draw_oxygen_bar(oxygen_percentage)
            ui.display_text(f"Level: {current_level_index + 1}", 10, 50)

            # Check for collisions with parts
            collected_parts = pygame.sprite.spritecollide(player, level.parts, True)
            if collected_parts:
                for part in collected_parts:
                    sounds.play_collect_sound()
                    player_score += 1  # Increase score for collecting parts

            # Check if the player falls off the screen
            if player.rect.y > SCREEN_HEIGHT:
                print("You fell off the platform!")
                player.respawn()  # Respawn the player

            # Check for level completion
            if player_score >= 10:  # All parts collected
                print(f"Level {current_level_index + 1} complete!")
                sounds.play_finish_sound()
                break

            pygame.display.flip()
            clock.tick(FPS)

        # Save score to leaderboard
        leaderboard.add_score(player_name, player_score)

        # Prepare for the next level
        current_level_index += 1
        if current_level_index >= 5:  # Maximum levels
            print("Game Over! You've completed all levels.")
            break

    pygame.quit()

if __name__ == "__main__":
    main()
