#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame

from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((801, 711))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()  # Capture the return value from the menu

            # If menu_return is a valid menu option, you can proceed to the next step
            if menu_return == 'Level':
                # Example level flow (level details will depend on your specific logic)
                # player_score = [0, 0]
                # level = Level(self.window, 'Level1', menu_return, player_score)
                # level_return = level.run(player_score)
                pass  # Handle Level 1 or other options

            elif menu_return == 'Exit':
                pygame.quit()
                quit()  # End pygame
            elif menu_return == 'Score':
                # Handle displaying scores, if needed
                pass
