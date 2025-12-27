#!/usr/bin/env python3

import pygame
import constants
from logger import log_state


def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: VERSION{pygame.version.ver}")
    #print(f"Screen width: {constants.SCREEN_WIDTH}")
    #print(f"Screen height: {constants.SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    while():
        log_state()
        screen.fill("black")
        pygame.display.flip()
        


if __name__ == "__main__":
    main()
