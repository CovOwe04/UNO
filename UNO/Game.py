# Owen Covach, Katarina Lukic, Yilin Xu
# Module 14 Final Project "UNO"

#importing pygame into the program
import pygame
from pygame.locals import *

#initiates pygame
pygame.init()

#setting a pygame clock variable to set a framrate for the game
clock = pygame.time.Clock()
fps = 60

#creating a screen width and height variables
screen_width, screen_height = 1000, 600

#creating a screen at the set width and height
screen = pygame.display.set_mode((screen_width, screen_height))
#sets a title for the window
pygame.display.set_caption('UNO!')

#setting a variable to check if in the main menu or not
main_menu = True
#setting a variable to check if in the instructions or not
instructions = True
#setting a variable to check if the user clicked singleplayer or multiplayer or if the game ended
Gameplay = 0

#creating a font to use to draw
font = pygame.font.SysFont('impact', 36)

#defining a bunch of colours to make colouring things in code easier
White = (255,255,255)
Black = (0,0,0)
Yellow = (255,255,0)


bg_img = pygame.image.load('UNO/UNO_bg.jpg').convert_alpha()
title_img = pygame.image.load('UNO/UNO_title.png').convert_alpha()
singleplayer_img = pygame.image.load('UNO/start_btn.png').convert_alpha()
singleplayer_img_hover = pygame.image.load('UNO/start_btn_hover.png').convert_alpha()
multiplayer_img = pygame.image.load('UNO/start_btn2.png').convert_alpha()
multiplayer_img_hover = pygame.image.load('UNO/start_btn2_hover.png').convert_alpha()
play_img = pygame.image.load('UNO/play_btn.png').convert_alpha()
play_img_hover = pygame.image.load('UNO/play_btn_hover.png').convert_alpha()

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

class Button():
    #this function is the creation of the button itself, its called when the class is called
    def __init__(self, x, y, image):
        #sets the button's image to the given image
        self.image = image

        #sets a rectangle to be the size of the image size(width x height). used for collision
        self.rect = self.image.get_rect()

        #sets the x and y coordinates of the rectangle to the given points
        self.rect.x = x
        self.rect.y = y

        #setting a variable to check if a button is clicked
        self.clicked = False
   
    #this function checks for collision as well as draws the button onto the window
    def draw(self, image, image2):

        #creating a variable for returning an action by the user to the main program
        action = False

        #gets mouse position, sets it to a variable
        pos = pygame.mouse.get_pos()

        #checks if the mouse is over the button
        if self.rect.collidepoint(pos):
            #if the mouse is on the button, set the image to the hover image
            self.image = image 

            #checks if the mouse is clicked and if it isnt already clicked
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:

                #sets the action to return and that the mouse has been clicked as true
                action = True
                self.clicked = True
        
        #if mouse if not over button, set the image to the original button image
        else:
            self.image = image2        

        #checks if the mouse isnt pressed
        if pygame.mouse.get_pressed()[0] == 0:
            #sets the click variable as false so the computer knows its not pressed
            self.clicked = False
        

        #draw button
        screen.blit(self.image, self.rect)

        return action


Singleplayer_btn = Button(330, 270, singleplayer_img)
Multiplayer_btn = Button(330, 400, multiplayer_img)
Play_btn = Button(330, 450, play_img)

run = True
while run == True:
    screen.blit(pygame.transform.scale(bg_img,(screen_width,screen_height)), (0,0))

    if Gameplay == 0:
        main_menu = True
        instructions = True

    if Gameplay == 1:
        if instructions == True:
            draw_text('Instructions', font, Yellow, 420, 10)
            if Play_btn.draw(play_img_hover, play_img):
                instructions = False
                pygame.time.delay(100)
                screen.blit(pygame.transform.scale(bg_img,(screen_width,screen_height)), (0,0))
                

    elif Gameplay == 2:
        if instructions == True:
            draw_text('Instructions', font, White, 420, 10)
            if Play_btn.draw(play_img_hover, play_img):
                instructions = False
                pygame.time.delay(100)
                screen.blit(pygame.transform.scale(bg_img,(screen_width,screen_height)), (0,0))
                

    if main_menu == True:
        screen.blit(pygame.transform.scale(title_img,(320,225)), (340,40))
        if Singleplayer_btn.draw(singleplayer_img_hover, singleplayer_img):
            main_menu = False
            Gameplay = 1
            pygame.time.delay(100)
            screen.blit(pygame.transform.scale(bg_img,(screen_width,screen_height)), (0,0))

        if Multiplayer_btn.draw(multiplayer_img_hover, multiplayer_img):
            main_menu = False
            Gameplay = 2
            pygame.time.delay(100)
            screen.blit(pygame.transform.scale(bg_img,(screen_width,screen_height)), (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    clock.tick(fps)
    pygame.display.update()
    

pygame.quit()