import pygame

#Initialization
pygame.init()
display_width = 685
display_height = 600
window_title = "Smart Parking"

#Color
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
BLUE = (0,0,225)
GREEN = (0,255,0)

#System Property
margin = 1
block = 20

#Setup
window = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Smart Parking")
clock=pygame.time.Clock()
