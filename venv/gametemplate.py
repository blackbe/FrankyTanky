import pygame
import time
import random
import os
import sys

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

display_width = 800
display_height = 600

appleThickness = 30
block_size = 20
FPS = 10

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Franky Tanky')

# icon = pygame.image.load(resource_path("icon.png"))  # should be 32 by 32
# pygame.display.set_icon(icon)
#
#
# img = pygame.image.load(resource_path("snakehead.png"))
# appleimg = pygame.image.load(resource_path("apple.png"))


clock = pygame.time.Clock()


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def pause():
    global FPS
    paused = True
    message_to_screen("Paused",
                      black,
                      -100,
                      size="large")
    message_to_screen("Press 1, 2, 3, or 4 to continue or Q to quit.",
                      black,
                      25)
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitScreen()
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    FPS = 5
                    paused = False
                if event.key == pygame.K_2:
                    FPS = 10
                    paused = False
                if event.key == pygame.K_3:
                    FPS = 15
                    paused = False
                if event.key == pygame.K_4:
                    FPS = 25
                    paused = False
                elif event.key == pygame.K_q:
                    quitScreen()
                    pygame.quit()
                    quit()

        clock.tick(5)


def quitScreen():
    gameDisplay.fill(white)
    message_to_screen("Have a wonderful day!",
                      green,
                      size="medium")
    pygame.display.update()
    time.sleep(2)  # not going to keep this here
    return


def score(score):
    text = smallfont.render("Score: " + str(score), True, black)
    gameDisplay.blit(text, [0, 0])


def game_intro():
    intro = True
    global FPS

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitScreen()
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    FPS = 5
                    intro = False
                if event.key == pygame.K_2:
                    FPS = 10
                    intro = False
                if event.key == pygame.K_3:
                    FPS = 15
                    intro = False
                if event.key == pygame.K_4:
                    FPS = 25
                    intro = False
                if event.key == pygame.K_q:
                    quitScreen()
                    pygame.quit()
                    quit()
        gameDisplay.fill(white)
        message_to_screen("Welcome to Franky Tanky",
                          green,
                          -120,
                          size="medium")
        message_to_screen("The objective is to shoot and destroy",
                          black,
                          -50)
        message_to_screen("the enemy tank before they destroy you.",
                          black,
                          -10)
        message_to_screen("The more enemies you destroy the harder they get.",
                          black,
                          20)
        message_to_screen("Choose your skill level by pressing one of the following:",
                          black,
                          50)
        message_to_screen("1: Beginner, 2: Intermediate, 3: Advanced, 4: Professional",
                          black,
                          100)
        message_to_screen("Press P to pause, or Q to quit",
                          black,
                          130)
        pygame.display.update()
        clock.tick(10)


def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width / 2), (display_height / 2) + y_displace
    gameDisplay.blit(textSurf, textRect)


def gameLoop():
    global direction
    global FPS

    direction = "right"
    gameExit = False
    gameOver = False

    while not gameExit:
        if gameOver == True:
            message_to_screen("Game over",
                              red,
                              y_displace=-50,
                              size="large")
            message_to_screen("Press 1, 2, 3, or 4 to play again or Q to quit",
                              black,
                              y_displace=50,
                              size="small")
            pygame.display.update()

        while gameOver == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    elif event.key == pygame.K_1:
                        FPS = 5
                        gameLoop()
                    elif event.key == pygame.K_2:
                        FPS = 10
                        gameLoop()
                    elif event.key == pygame.K_3:
                        FPS = 15
                        gameLoop()
                    elif event.key == pygame.K_4:
                        FPS = 25
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pass
                elif event.key == pygame.K_RIGHT:
                    pass
                elif event.key == pygame.K_UP:
                    pass
                elif event.key == pygame.K_DOWN:
                    pass
                elif event.key == pygame.K_p:
                    pause()

        gameDisplay.fill(white)

        pygame.display.update()

        clock.tick(FPS)

    quitScreen()
    pygame.quit()
    quit()


game_intro()
gameLoop()