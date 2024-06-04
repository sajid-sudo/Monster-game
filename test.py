import pygame as pg
import sys

pg.init()

# Set up the display
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Pygame Window")

# Main loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Fill the screen with black
    pg.display.flip()

pg.quit()
sys.exit()
