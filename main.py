#!/usr/bin/env python3

import pygame
import constants
from logger import log_state


def main():
    pygame.init()
    fps_clock = pygame.time.Clock()
    dt = 0
    print(f"Starting Asteroids with pygame version: VERSION{pygame.version.ver}")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, 
                                      constants.SCREEN_HEIGHT))
    while(True):
        #calls log
        log_state()
        #shuts screen down if exit clicked
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #fills and updates screen
        screen.fill("black")
        pygame.display.flip()
        #updates the screen + updates delta value (since last frame was drawn)
        dt = (fps_clock.tick(60)/1000)
        #print(dt)
        


if __name__ == "__main__":
    main()
