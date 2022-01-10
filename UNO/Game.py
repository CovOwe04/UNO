# Owen Covach, Katarina Lukic, Yilin Xu
# Module 14 Final Project "UNO"

#importing pygame into the program
import pygame
from pygame.locals import *
import random

#initiates pygame
pygame.init()

#setting a pygame clock variable to set a framerate for the game
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

#defining a bunch of colours to make colouring things in code easier (uses RGB values to make colours)
White = (255,255,255)
Black = (0,0,0)
Yellow = (255,255,0)
Blue = (0,0,255)

#setting variables as images to use later (convert_alpha is a function that helps make the game run smoother)
bg_img = pygame.image.load('UNO/UNO_bg.jpg').convert_alpha()
title_img = pygame.image.load('UNO/UNO_title.png').convert_alpha()
singleplayer_img = pygame.image.load('UNO/start_btn.png').convert_alpha()
singleplayer_img_hover = pygame.image.load('UNO/start_btn_hover.png').convert_alpha()
multiplayer_img = pygame.image.load('UNO/start_btn2.png').convert_alpha()
multiplayer_img_hover = pygame.image.load('UNO/start_btn2_hover.png').convert_alpha()
play_img = pygame.image.load('UNO/play_btn.png').convert_alpha()
play_img_hover = pygame.image.load('UNO/play_btn_hover.png').convert_alpha()

def draw_text(text, font, text_col, x, y):

    #setting a variable as the text that is given and renders is with a colour
    img = font.render(text, True, text_col)

    #draws the text on the window
    screen.blit(img, (x, y))
    
class deck():
   
    colours = ["Red", "Green", "Yellow", "Blue"]
    deckcards = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Draw two", "Reverse Card", "Skip Card", "Colour Wheel", "Pick up 4"]
    
        

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

#creating buttons and giving coordinates to place them on the window and an image to display
Singleplayer_btn = Button(330, 270, singleplayer_img)
Multiplayer_btn = Button(330, 400, multiplayer_img)
Play_btn = Button(330, 450, play_img)

#starts the game loop
run = True
while run == True:

    #runs this if statement if the gameplay variable is 0 (start of program or game over)
    if Gameplay == 0:
        #prints the background first before the other images
        screen.blit(pygame.transform.scale(bg_img,(screen_width,screen_height)), (0,0))

        #sets the main menu and instructions variable to true to make them reappear
        main_menu = True
        instructions = True

    #runs this if statement if the gameplay variable is 1 (player selected singleplayer)
    elif Gameplay == 1:
        #prints the background first before the other images
        screen.blit(pygame.transform.scale(bg_img,(screen_width,screen_height)), (0,0))
        if instructions == True:
            draw_text('Instructions', font, White, 420, 10)
            if Play_btn.draw(play_img_hover, play_img):
                instructions = False
                pygame.time.delay(100)
                screen.blit(pygame.transform.scale(bg_img,(screen_width,screen_height)), (0,0))
                
    #runs this if statement if the gameplay variable is 2 (player selected singleplayer)
    elif Gameplay == 2:

        #prints the background first before the other images
        screen.blit(pygame.transform.scale(bg_img,(screen_width,screen_height)), (0,0))

        #checks if the instructions variable is true
        if instructions == True:

            #displays the text for the instructions of the game
            draw_text('Instructions', font, White, 420, 10)

            #checks if the player has pressed the play button
            if Play_btn.draw(play_img_hover, play_img):

                #sets the instructions variable as false
                instructions = False

                #delays button reaction for 100 milliseconds
                pygame.time.delay(100)

                #
                screen.blit(pygame.transform.scale(bg_img,(screen_width,screen_height)), (0,0))
                #start coding here
                

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
