import pygame

# Init the pygame
pygame.init()

# create a screen
screen = pygame.display.set_mode((800, 600))

# title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('space-game.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

def player(x,y):
    screen.blit(playerImg, (x,y))

# Game Loop
running = True
while running:
    screen.fill((255,128,35))  # RGB 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left Key pressed")
                playerX_change = -0.2
            if event.key == pygame.K_RIGHT:
                print("Right Key Pressed")
                playerX_change = 0.2
            if event.key == pygame.K_UP:
                print("Up Key Pressed")
                playerY_change = -0.2
            if event.key == pygame.K_DOWN:
                print("Down Key Pressed")
                playerY_change = 0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerX_change = 0
                playerY_change = 0
               
            
 

   
    playerX += playerX_change
    playerY += playerY_change
    player(playerX, playerY)
    pygame.display.update()