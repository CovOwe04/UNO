# Owen Covach, Katarina Lukic, Yilin X
# Module 14 Final Project "WAR"

#importing pygame into the program
import pygame
from pygame.locals import *
import random

#initiates pygame
pygame.init()

#setting a pygame clock variable to set a framerate for the game
clock = pygame.time.Clock()
#fps = Frames per second
fps = 60

#creating a screen width and height variables, width is 1000 and height is 600
screen_width, screen_height = 1000, 600

#creating a display screen at the set width and height
screen = pygame.display.set_mode((screen_width, screen_height))

#sets a title for the window
pygame.display.set_caption('WAR!')

#setting a variable to check if the program is in the main menu or not
main_menu = True

#setting a variable to check if in the program is in instructions or not
instructions = True

#setting a variable to check if the user clicked singleplayer, multiplayer or if the game has ended
Gameplay = 0

#creating a font for all  text in the game, with a size of 36 pixels
font = pygame.font.SysFont('impact', 36)

#defining the colours for the main menu White, Black, Yellow, Blue(uses RGB values to make colours)
#RGB is how much of either Red, Blue or Green a colour has, the higher the number the higher the saturation
White = (255,255,255)
Black = (0,0,0)
Yellow = (255,255,0)
Blue = (0,0,255)

#setting variables as images to use for the title, single player or mulitplayer(convert_alpha is a function that helps make the game run smoother)
bg_img = pygame.image.load('Assets/WAR_bg.jpg').convert_alpha()
title_img = pygame.image.load('Assets/WAR_title.png').convert_alpha()
singleplayer_img = pygame.image.load('Assets/start_btn.png').convert_alpha()
singleplayer_img_hover = pygame.image.load('Assets/start_btn_hover.png').convert_alpha()
multiplayer_img = pygame.image.load('Assets/start_btn2.png').convert_alpha()
multiplayer_img_hover = pygame.image.load('Assets/start_btn2_hover.png').convert_alpha()
continue_img = pygame.image.load('Assets/play_btn.png').convert_alpha()
continue_img_hover = pygame.image.load('Assets/play_btn_hover.png').convert_alpha()

#defining a function named draw_text that draws the text and font on the coordinate plane 
def draw_text(text, font, text_col, x, y):
    #setting a variable as the text that is given and renders is with a colour
    img = font.render(text, True, text_col)

    #draws the text on the display window
    screen.blit(img, (x, y))     
    screen.blit(img, (x, y))
    
#creates a class for the button in regards to the location, size and if it is clicked or not
class MenuButton():
    #this function is the creation of the button itself, its called when the class is called
    def __init__(self, x, y, image):
        #sets the button's image to the given image
        self.image = image

        #sets a rectangle to be the size of the image size(width x height). used for mouse detection
        self.rect = self.image.get_rect()

        #sets the x and y coordinates of the rectangle to the given values on lines 140 - 142
        self.rect.x = x
        self.rect.y = y

        #setting a variable to check if a button is clicked or not
        self.clicked = False
   
    #this function checks for collision as well as draws the button onto the window
    def draw(self, image, image2):

        #creating a variable for returning an action by the mouse to the main program
        action = False

        #gets the mouse position, sets it to a variable named pos
        pos = pygame.mouse.get_pos()

        #checks if the mouse is hovering over the button
        if self.rect.collidepoint(pos):
            #if the mouse is on the button, set the image to the hover image
            self.image = image 

            #checks if the mouse is clicked and if it isnt already clicked
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:

                #sets the action to return and that the mouse has been clicked as true
                action = True
                self.clicked = True
        
        #if mouse if not over button, set the image to the original button image unaltered
        else:
            self.image = image2        

        #checks if the mouse isnt pressed
        if pygame.mouse.get_pressed()[0] == 0:
            #sets the click variable as false so the computer knows its not pressed
            self.clicked = False
        

        #drawing the button
        screen.blit(self.image, self.rect)

        return action

def Singleplayer(instructions):
    #prints the background first before the other images so there is no overlap
        screen.blit(pygame.transform.scale(bg_img,(screen_width,screen_height)), (0,0))

        #checks if the instructions variable is true
        if instructions == True:

            #displays the text for the instructions of the game
            draw_text('Instructions', font, White, 420, 10)

            #checks if the player has pressed the play button
            if Continue_btn.draw(continue_img_hover, continue_img):

                #sets the instructions variable as false
                instructions = False

                #delays button reaction for 100 milliseconds so it is not instatanous 
                pygame.time.delay(100)

                #draws the background image onto the window
                screen.blit(pygame.transform.scale(bg_img,(screen_width,screen_height)), (0,0))
                

                #shuffles then deals deck
                for x in range(0,54):
                    rand = random.randint(x,53)
                    
                    temp = Game_deck[x]
                    Game_deck[x] = Game_deck[rand]
                    Game_deck[rand] = temp
                
                for x in range(0,27):
                    Player1.append(Game_deck[2 * x])
                    Player2.append(Game_deck[2 * x + 1])

                #reads key presses then adds the top card in the player deck to play 
                for event in pygame.event.get():

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                            Play1.append[Player1[0]]
                            Player1.remove(Player1[0])

                        if event.key == pygame.K_l:
                            Play2.append[Player2[0]]
                            Player2.remove(Player2[0])
                

def Multiplayer(instructions):
    #prints the background first before the other images so there is no overlap
        screen.blit(pygame.transform.scale(bg_img,(screen_width,screen_height)), (0,0))

        #checks if the instructions variable is true
        if instructions == True:

            #displays the text for the instructions of the game
            draw_text('Instructions', font, White, 420, 10)

            #checks if the player has pressed the play button
            if Continue_btn.draw(continue_img_hover, continue_img):

                #sets the instructions variable as false
                instructions = False

                #delays button reaction for 100 milliseconds so it is not instatanous 
                pygame.time.delay(100)

                #draws the background image onto the window
                screen.blit(pygame.transform.scale(bg_img,(screen_width,screen_height)), (0,0))
                
                #shuffles then deals deck
                for x in range(0,54):
                    rand = random.randint(x,53)
                    
                    temp = Game_deck[x]
                    Game_deck[x] = Game_deck[rand]
                    Game_deck[rand] = temp
                
                for x in range(0,27):
                    Player1.append(Game_deck[2 * x])
                    Player2.append(Game_deck[2 * x + 1])
                
                #reads key presses then adds the top card in the player deck to play 
                for event in pygame.event.get():

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                            Play1.append[Player1[0]]
                            Player1.remove(Player1[0])

                        if event.key == pygame.K_l:
                            Play2.append[Player2[0]]
                            Player2.remove(Player2[0])
                


#creating lists for Player decks and play deck
Game_deck = []
Player1 = []
Player2 = []
Play1 = []
Play2 = []

#creates deck
for x in range(1,14):
    for z in range(1,5):
        Game_deck.append(x)
Game_deck.append(14)
Game_deck.append(14)

#creating buttons and giving coordinates to place them on the window and an image to display
Singleplayer_btn = MenuButton(330, 270, singleplayer_img)
Multiplayer_btn = MenuButton(330, 400, multiplayer_img)
Continue_btn = MenuButton(330, 450, continue_img)

#starts the main game loop
run = True
while run == True:
    print(Game_deck)
    #runs this if statement if the gameplay variable is 0 (start of program or game over)
    if Gameplay == 0:
        #prints the background first before the other images so there is no overlap
        screen.blit(pygame.transform.scale(bg_img,(screen_width,screen_height)), (0,0))

        #sets the main menu and instructions variable to true to make them reappear
        main_menu = True
        instructions = True

    #runs this if statement if the gameplay variable is 1 (player selected singleplayer mode)
    elif Gameplay == 1:

        #starts the singleplayer function which is the singleplayer gamemode against a "bot"
        Singleplayer(instructions)
                
    #runs this if statement if the gameplay variable is 2 (player selected multiplayer mode)
    elif Gameplay == 2:
        
        #starts the multiplayer function which is the multiplayer gamemode against another person
        Multiplayer(instructions)


                
    #runs the section if the main menu variable is true
    if main_menu == True:

        #draws the background image before anything else
        screen.blit(pygame.transform.scale(title_img,(320,225)), (340,40))

        #checks if the singleplayer button was pressed
        if Singleplayer_btn.draw(singleplayer_img_hover, singleplayer_img):

            #sets the main menu variable to false(stops the main menu screen loop)
            main_menu = False

            #sets the Gameplay variable to 1 (singleplayer game)
            Gameplay = 1

            #delays button reaction by 100 milliseconds
            pygame.time.delay(100)

            #draws the background image to remove the menu images
            screen.blit(pygame.transform.scale(bg_img,(screen_width,screen_height)), (0,0))

        #checks if the multiplayer button was pressed
        if Multiplayer_btn.draw(multiplayer_img_hover, multiplayer_img):

            #sets the main menu variable to false(stops the main menu screen loop)
            main_menu = False

            #sets the Gameplay variable to 2 (multiplayer game)
            Gameplay = 2

            #delays button reaction by 100 milliseconds
            pygame.time.delay(100)

            #draws that background image to remove menu images
            screen.blit(pygame.transform.scale(bg_img,(screen_width,screen_height)), (0,0))

    # if the player has quit the game then the program with close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #sets a framerate for the computer to run at
    clock.tick(fps)

    #updates the pygame display after each user input
    pygame.display.update()
    
    
# closes the pygame application
pygame.quit()
