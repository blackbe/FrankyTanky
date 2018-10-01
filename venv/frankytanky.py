import pygame
import time
import random
import os
import sys


pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

red = (180, 0, 0)
light_red = (255, 0, 0)

yellow =(200, 200, 0)
light_yellow = (255, 255, 0)

green = (0, 155, 0)
light_green = (0, 255, 0)

display_width = 800
display_height = 600

FPS = 10

mainTankX = display_width * 0.9
mainTankY = display_height * 0.9

tankWidth = 40
tankHeight = 20

turretWidth = 3
wheelWidth = 5

smallfont = pygame.font.SysFont("stencil", 15)
medfont = pygame.font.SysFont("stencil", 25)
largefont = pygame.font.SysFont("stencil", 50)

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
    message_to_screen("Thanks for playing!",
                      green,
                      size="medium")
    pygame.display.update()
    time.sleep(2)
    return


def score(score):
    text = smallfont.render("Score: " + str(score), True, black)
    gameDisplay.blit(text, [0, 0])


def game_intro():
    global FPS
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitScreen()
                pygame.quit()
                quit()


        gameDisplay.fill(white)
        message_to_screen("Welcome to Franky Tanky!",
                          green,
                          -120,
                          size="large")
        message_to_screen("The objective is to shoot and destroy",
                          black,
                          -40)
        message_to_screen("the enemy tank before they destroy you.",
                          black,
                          -10)
        message_to_screen("The more enemies you destroy, the harder they get.",
                          black,
                          20)

        button("play", 150, 500, 100, 50, green, light_green, action="play")
        button("controls", 350, 500, 100, 50, yellow, light_yellow, action="controls")
        button("quit", 550, 500, 100, 50, red, light_red, action="quit")

        message_to_screen("Press P to pause, or Q to quit",
                          black,
                          160)
        pygame.display.update()
        clock.tick(FPS)


def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()


def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = ((buttonx + (buttonwidth / 2)), (buttony + (buttonheight / 2)))
    gameDisplay.blit(textSurf, textRect)


def message_to_screen(msg, color, y_displace=0, size="medium"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width / 2), (display_height / 2) + y_displace
    gameDisplay.blit(textSurf, textRect)


def tank(x, y):
    x = int(x)
    y = int(y)
    pygame.draw.circle(gameDisplay, yellow, (x , y), int(tankHeight / 2))
    pygame.draw.rect(gameDisplay, yellow, (x - tankHeight, y, tankWidth, tankHeight))

    pygame.draw.line(gameDisplay, yellow, (x, y), (x - 10, y - 15), turretWidth)

    #pygame.draw.circle(gameDisplay, yellow, (x - 15, y + 20), wheelWidth)

    for x in range(-20,25, 5):
        pygame.draw.circle(gameDisplay, yellow, (int(mainTankX) + x, y + 20), wheelWidth)


def game_controls():
    gcont = True

    while gcont:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitScreen()
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        message_to_screen("Controls",
                          green,
                          -120,
                          size="large")
        message_to_screen("Fire: Spacebar",
                          black,
                          -40)
        message_to_screen("Move Turret: Up and Down arrows",
                          black,
                          -10)
        message_to_screen("Move Tank: Left and Right arrows",
                          black,
                          20)
        message_to_screen("Pause: P", black, 90)

        button("play", 150, 500, 100, 50, green, light_green, action="play")
        button("main", 350, 500, 100, 50, yellow, light_yellow, action="main")
        button("quit", 550, 500, 100, 50, red, light_red, action="quit")

        pygame.display.update()
        clock.tick(15)

def button(text, x, y, width, height, inactive_color, active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()
            if action == "controls":
                game_controls()
            if action == "play":
                gameLoop()
            if action == "main":
                game_intro()
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))

    text_to_button(text, black, x, y, width, height)

def gameLoop():
    global FPS
    global direction

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

        tank(mainTankX, mainTankY)

        pygame.display.update()

        clock.tick(FPS)

    quitScreen()
    pygame.quit()
    quit()

game_intro()
gameLoop()

