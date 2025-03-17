import pygame
from pygame import Surface, Rect
from pygame.font import Font

# Constants for colors
C_PINK = (255, 105, 180)
C_WHITE = (255, 255, 255)


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

        # Menu options
        self.menu_options = ['Level', 'Score', 'Exit']
        self.selected_option = 0  # Track the selected option

        # Initialize pygame mixer for music
        pygame.mixer.init()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        """Render and display the menu text"""
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def run(self):
        pygame.mixer_music.load('./asset/Menu.mp3')  # Ensure the file path is correct
        pygame.mixer_music.play(-1)  # Loop music indefinitely

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Handle key press events for navigation
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(self.menu_options)
                    elif event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(self.menu_options)
                    elif event.key == pygame.K_RETURN:
                        return_value = self.menu_options[self.selected_option]
                        if return_value == 'Exit':
                            running = False  # Exit the game when 'Exit' is selected
                        return return_value

            # DRAW IMAGES
            self.window.fill((0, 0, 0))  # Clear the screen with a black background
            self.window.blit(self.surf, self.rect)

            # Draw the menu title
            self.menu_text(100, "Wrath", (255, 255, 255), ((811 / 2), 100))
            self.menu_text(100, "Booh!", (255, 255, 255), ((811 / 2), 200))

            # Calculate the center of the screen dynamically
            x_pos = self.window.get_width() // 2  # Get the screen width and divide by 2 for center

            # Draw menu options
            for i, option in enumerate(self.menu_options):
                # Calculate Y position dynamically, starting at 300 and adding space based on the font size
                y_pos = 300 + (i * 60)  # Increased space (60) to avoid overlap based on the font size

                # Render the selected option with a different color
                if i == self.selected_option:
                    self.menu_text(50, option, C_PINK, (x_pos, y_pos))  # Selected option with ROSA color
                else:
                    self.menu_text(50, option, C_WHITE, (x_pos, y_pos))  # Unselected options with WHITE color

            pygame.display.flip()

        pygame.quit()  # Clean up pygame
        return None  # In case we exit without selecting an option
