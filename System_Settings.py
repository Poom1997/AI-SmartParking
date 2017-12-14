import pygame
import os

#Initialization
pygame.init()
display_width = 715
display_height = 527
window_title = "Smart Parking"

#Color
WHITE = (192,192,192)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
PURPLE = (229,0,255)
BLUE = (0,0,225)
GREEN = (0,255,0)
CYAN = (92, 247, 223)

#Font
font1 = pygame.font.SysFont("Times New Roman, Arial", 30)
font2 = pygame.font.SysFont("Times New Roman, Arial", 20)
font3 = pygame.font.SysFont("Times New Roman, Arial", 60)

#Text in EditMap
panelText = font1.render("Menu Panel",True, WHITE)
parkingText = font1.render("Car Park",True, BLACK)
wallText = font1.render("Wall",True, BLACK)
entranceText = font1.render("Entrance",True,WHITE)
exitText = font1.render("Exit",True,BLACK)
pathText = font1.render("Path",True,BLACK)


saveText = font2.render("Save",True,BLACK)
loadText = font2.render("Load",True,BLACK)
backText = font2.render("Back",True,BLACK)


#Text in Simulation
carEntranceText1 = font1.render("Available Slot",True,CYAN)
carEntranceText2 = font1.render("No. of Car",True,CYAN)
decText1 = font3.render("-",True,BLACK)
incText1 = font3.render("+",True,BLACK)
decText2 = font3.render("-",True,BLACK)
incText2 = font3.render("+",True,BLACK)

startText = font1.render("Start!",True,BLACK)
stopText = font1.render("Stop/Pause",True,BLACK)
backText2 = font1.render("Back",True,BLACK)


#picture
menuPic = pygame.image.load(os.path.join("photo","backgroundMenu.png"))
mainMenuPic = pygame.image.load(os.path.join("photo","mainMenu.png"))

editButtonPic = pygame.image.load(os.path.join("photo","createButton.png"))
simulateButtonPic = pygame.image.load(os.path.join("photo","simulateButton.png"))
exitButtonPic = pygame.image.load(os.path.join("photo","exitButton.png"))


#Picture Sign
entranceSign = pygame.image.load(os.path.join("photo","entranceSign.png"))
wallSign = pygame.image.load(os.path.join("photo","wallSign.png"))
parkingSign = pygame.image.load(os.path.join("photo","parkingSign.png"))
exitSign = pygame.image.load(os.path.join("photo","exitSign.png"))
pathSign = pygame.image.load(os.path.join("photo","pathSign.png"))
carInSign = pygame.image.load(os.path.join("photo","carInSign.png"))




#System Property
margin = 1
block = 20

#Setup
global window
window = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Smart Parking")
clock=pygame.time.Clock()
