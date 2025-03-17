#!/usr/bin/python
# -*- coding: utf-8 -*-

from Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.window_width = None
        self.rect = None

    def move(self):
        ENTITY_SPEED = {
            'Level1Bg1': 0,
            'Level1Bg2': 1,
            'Level1Bg3': 2,
            'Level1Bg4': 3,
            'Level1Bg5': 4,
            'Level1Bg6': 5,
            'Level1Bg7': 6,
            'Level1Bg8': 7,
            'Level1Bg9': 8
        }

        # Move the entity based on the name's speed
        self.rect.centerx -= ENTITY_SPEED.get(self.name, 0)  # Default to 0 if name not found

        # If the entity moves off the left side of the screen, reset its position
        if self.rect.right <= 0:
            self.rect.left = self.window_width  # Reset to the right side of the screen


