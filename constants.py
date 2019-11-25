#!/usr/bin/env python3

# Created by: Joseph Palermo
# Created on: October 2019
# This program makes sure that the sprite doesn’t go off the screen


SCREEN_X = 160
SCREEN_Y = 128
SCREEN_GRID_X = 16
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
TOTAL_NUMBER_OF_ALIENS = 8
TOTAL_NUMBER_OF_LASERS = 5
SHIP_SPEED = 1
ALIEN_SPEED = 1
OFF_SCREEN_X = -100
OFF_SCREEN_Y = -100
LASER_SPEED = 2
OFF_TOP_OF_SCREEN = -1 * SPRITE_SIZE
OFF_BOTTOM_OF_SCREEN = SCREEN_Y + SPRITE_SIZE
FPS = 60

NEW_PALETTE = (b'\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff'
b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')

# Using for button space
button_state = {
    "button_up": "up,",
    "button_just_pressed": "just pressed",
    "button_still_pressed": "still pressed",
    "button_released": "released"
}
