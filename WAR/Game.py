# Owen Covach, Katarina Lukic, Yilin Xu
# Module 14 Final Project "WAR"

#importing pygame into the program
import pygame
from pygame.locals import *
import random

#initiates pygame and fonts
pygame.init()
pygame.font.init()

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
wartime_font = pygame.font.SysFont('impact', 200)
Countdown_font = pygame.font.SysFont('comicsans', 50)

#defining the colours for the main menu White, Black, Yellow, Blue(uses RGB values to make colours)
#RGB is how much of either Red, Blue or Green a colour has, the higher the number the higher the saturation
White = (255,255,255)
Black = (0,0,0)
Yellow = (255,255,0)
Blue = (0,0,255)
Red = (255,0,0)

#setting variables as images to use for the title, single player or mulitplayer(convert_alpha is a function that helps make the game run smoother)
bg_img = pygame.image.load('Assets/WAR_bg.jpg').convert_alpha()
title_img = pygame.image.load('Assets/WAR_title.png').convert_alpha()
singleplayer_img = pygame.image.load('Assets/start_btn.png').convert_alpha()
singleplayer_img_hover = pygame.image.load('Assets/start_btn_hover.png').convert_alpha()
multiplayer_img = pygame.image.load('Assets/start_btn2.png').convert_alpha()
multiplayer_img_hover = pygame.image.load('Assets/start_btn2_hover.png').convert_alpha()
rules_img = pygame.image.load('Assets/rules_btn.png').convert_alpha()
rules_img_hover = pygame.image.load('Assets/rules_btn_hover.png').convert_alpha()
continue_img = pygame.image.load('Assets/continue_btn.png').convert_alpha()
continue_img_hover = pygame.image.load('Assets/continue_btn_hover.png').convert_alpha()
Card_back_img = pygame.image.load('Assets/BACK.png').convert_alpha()
Card_back_img = pygame.transform.scale(Card_back_img,(150, 200))
Discard_img = pygame.image.load('Assets/DISCARD.png').convert_alpha()
Ace_img =  pygame.image.load('Assets/1CARD.png').convert_alpha()
Ace_img = pygame.transform.scale(Ace_img,(150, 200))
Seven_img =  pygame.image.load('Assets/7CARD.png').convert_alpha()
Seven_img = pygame.transform.scale(Seven_img,(150, 200))
King_img =  pygame.image.load('Assets/13CARD.png').convert_alpha()
King_img = pygame.transform.scale(King_img,(150, 200))
Jack_img =  pygame.image.load('Assets/11CARD.png').convert_alpha()
Jack_img = pygame.transform.scale(Jack_img,(150, 200))

#defining a function named draw_text that draws the text and font on the coordinate plane 
def draw_text(text, font, text_col, x, y,):    #setting a variable as the text that is given and renders is with a colour
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

def Round_countdown():
    screen.blit(pygame.transform.scale(bg_img,(screen_width,screen_height)), (0,0))
    draw_text("Round "+str(roundnum), Countdown_font, White, 40, 20)
    draw_text('Player 1 Cards: ' +str(len(Player1)), font, Black, 380, 10)
    draw_text('Computer Cards: ' +str(len(Player2)), font, Black, 360, 540)
    draw_text("Press A to flip", font, Blue, 680, 10)
    screen.blit(pygame.transform.scale(Discard_img,(150, 200)), (150,220))
    screen.blit(pygame.transform.scale(Card_back_img,(150, 200)), (700,70))
    screen.blit(pygame.transform.scale(Card_back_img,(150, 200)), (700,330))
    if len(Discard) > 0:
        screen.blit(pygame.transform.scale(Card_back_img,(150, 200)), (150,220))
    draw_text("3", Countdown_font, White, 440, 240)
    pygame.display.update()
    pygame.time.delay(1000)
    draw_text("2", Countdown_font, White, 480, 240)
    pygame.display.update()
    pygame.time.delay(1000)
    draw_text("1", Countdown_font, White, 520, 240)
    pygame.display.update()
    pygame.time.delay(1000)
    draw_text("FLIP!", Countdown_font, White, 435, 290)
    pygame.display.update()
    pygame.time.delay(1000)
    screen.blit(pygame.transform.scale(bg_img,(screen_width,screen_height)), (0,0))
    draw_text("Round "+str(roundnum), Countdown_font, White, 40, 20)
    draw_text('Player 1 Cards: ' +str(len(Player1)), font, Black, 380, 10)
    draw_text('Computer Cards: ' +str(len(Player2)), font, Black, 360, 540)
    draw_text("Press A to flip", font, Blue, 680, 10)
    screen.blit(pygame.transform.scale(Discard_img,(150, 200)), (150,220))
    screen.blit(pygame.transform.scale(Card_back_img,(150, 200)), (700,70))
    screen.blit(pygame.transform.scale(Card_back_img,(150, 200)), (700,330))
    if len(Discard)>0:
        screen.blit(pygame.transform.scale(Card_back_img,(150, 200)), (150,220))
    for x1 in range(0,13):
        if Player2[0] == x1:
            screen.blit(pygame.transform.scale(pygame.image.load('Assets/'+str(x1)+'CARD.png'),(150, 200)), (420,320))
    pygame.display.update()

def Shuffle_deck():
    #shuffles then deals deck
        for x in range(0,52):
            rand = random.randint(x,52)
                                    
            #creates a random temoporary game deck to hold the cards in
            temp = Game_deck[x]
            Game_deck[x] = Game_deck[rand]
            Game_deck[rand] = temp
                                
        # a for loop that splits the cards in half (26 cards) and puts them at the end of their decks
        for x in range(0,26):
            Player1.append(Game_deck[2 * x])
            Player2.append(Game_deck[2 * x + 1])

def Handle_key_presses(clicked):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_a] and clicked == False and len(Play1) == 0:
        for x1 in range(0,13):
            if Player1[0] == x1:
                screen.blit(pygame.transform.scale(pygame.image.load('Assets/'+str(x1)+'CARD.png'),(150, 200)), (420,90))
                pygame.display.update()
                            

        Play1.append(Player1[0])
        Player1.remove(Player1[0])
        Play2.append(Player2[0])
        Player2.remove(Player2[0])
        clicked = True
    elif keys_pressed[pygame.K_a] == False or keys_pressed[pygame.K_a] == False:
        clicked = False

def Handle_war_round(roundnum, round_start):
    if Play1[0] > Play2[0]:
        draw_text("Round "+str(roundnum)+" Winner", font, Black, 380, 160)
        pygame.display.update()
        pygame.time.delay(2000)
        Player1.append(Play1[0])
        Player1.append(Play2[0])
        if len(Discard) > 0:
            for x3 in range(0,len(Discard)):
                Player1.append(Discard[0])
                Discard.remove(Discard[0])
        roundnum += 1
        round_start = True

    if Play1[0] < Play2[0]:
        draw_text("Round "+str(roundnum)+" Winner", font, Black, 380, 380)
        pygame.display.update()
        pygame.time.delay(2000)
        Player2.append(Play1[0])
        Player2.append(Play2[0])
        if len(Discard) > 0:
            for x3 in range(0,len(Discard)):
                Player1.append(Discard[0])
                Discard.remove(Discard[0])
        roundnum += 1
        round_start = True
                    
    if Play1[0] > 0 and Play2[0] > 0:
        if Play1[0] == Play2[0]:
            draw_text("WAR TIME!", wartime_font, Red, 120, 160)
            pygame.display.update()
            pygame.time.delay(2000)
            pygame.display.update()
            Discard.append(Play1[0])
            Discard.append(Play2[0])
            Discard.append(Player1[0])
            Discard.append(Player2[0])
            Player1.remove(Player1[0])
            Player2.remove(Player2[0])
            roundnum += 1
            round_start = True
    Play1.remove(Play1[0])
    Play2.remove(Play2[0])
    return round_start

def Multiplayer(round_start, clicked, Shuffled, roundnum, ):

    if Shuffled == False:
        
        #shuffles then deals deck
        for x in range(0,52):
            rand = random.randint(x,52)
                            
            #creates a random temoporary game deck to hold the cards in
            temp = Game_deck[x]
            Game_deck[x] = Game_deck[rand]
            Game_deck[rand] = temp
                        
        # a for loop that splits the cards in half (26 cards) and puts them at the end of their decks
        for x in range(0,26):
            Player1.append(Game_deck[2 * x])
            Player2.append(Game_deck[2 * x + 1])

        Shuffled = True
        
    if len(Player2) != 52 or len(Player2) != 52 or roundnum <= 200:
            
        if round_start == True:
            screen.blit(pygame.transform.scale(bg_img,(screen_width,screen_height)), (0,0))
            draw_text("Round "+str(roundnum), Countdown_font, White, 40, 20)
            draw_text('Player 1 Cards: ' +str(len(Player1)), font, Black, 380, 10)
            draw_text('Player 2 Cards: ' +str(len(Player2)), font, Black, 380, 540)
            draw_text("Press A to flip", font, Blue, 680, 10)
            draw_text("Press L to flip", font, Blue, 680, 540)
            screen.blit(pygame.transform.scale(Discard_img,(150, 200)), (150,220))
            screen.blit(pygame.transform.scale(Card_back_img,(150, 200)), (700,70))
            screen.blit(pygame.transform.scale(Card_back_img,(150, 200)), (700,330))
            if len(Discard) > 0:
                screen.blit(pygame.transform.scale(Card_back_img,(150, 200)), (150,220))
            draw_text("3", Countdown_font, White, 440, 240)
            pygame.display.update()
            pygame.time.delay(1000)
            draw_text("2", Countdown_font, White, 480, 240)
            pygame.display.update()
            pygame.time.delay(1000)
            draw_text("1", Countdown_font, White, 520, 240)
            pygame.display.update()
            pygame.time.delay(1000)
            draw_text("FLIP!", Countdown_font, White, 435, 290)
            pygame.display.update()
            pygame.time.delay(1000)
            screen.blit(pygame.transform.scale(bg_img,(screen_width,screen_height)), (0,0))
            draw_text("Round "+str(roundnum), Countdown_font, White, 40, 20)
            draw_text('Player 1 Cards: ' +str(len(Player1)), font, Black, 380, 10)
            draw_text('Player 2 Cards: ' +str(len(Player2)), font, Black, 380, 540)
            draw_text("Press A to flip", font, Blue, 680, 10)
            draw_text("Press L to flip", font, Blue, 680, 540)
            screen.blit(pygame.transform.scale(Discard_img,(150, 200)), (150,220))
            screen.blit(pygame.transform.scale(Card_back_img,(150, 200)), (700,70))
            screen.blit(pygame.transform.scale(Card_back_img,(150, 200)), (700,330))
            if len(Discard) > 0:
                screen.blit(pygame.transform.scale(Card_back_img,(150, 200)), (150,220))
            pygame.display.update()
            round_start = False
                            
        if len(Play1) == 0 and len(Play2) == 0 or len(Play1) == 1 and len(Play2) == 0 or len(Play1) == 0 and len(Play2) == 1:
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_a] and clicked == False and len(Play1) == 0:
                for x1 in range(0,13):
                    if Player1[0] == x1:
                        screen.blit(pygame.transform.scale(pygame.image.load('Assets/'+str(x1+1)+'CARD.png'),(150, 200)), (420,90))
                        pygame.display.update()
                Play1.append(Player1[0])
                Player1.remove(Player1[0])
                clicked = True
                print(Play1)
            elif keys_pressed[pygame.K_l] and clicked == False and len(Play2) == 0:
                for x2 in range(0,13):
                    if Player2[0] == x2:
                        screen.blit(pygame.transform.scale(pygame.image.load('Assets/'+str(x2+1)+'CARD.png'),(150, 200)), (420,320))
                        pygame.display.update()
                Play2.append(Player2[0])
                Player2.remove(Player2[0])
                clicked = True
                print(Play2)
            elif keys_pressed[pygame.K_a] == False or keys_pressed[pygame.K_a] == False:
                clicked = False

        if len(Play1) == 1 and len(Play2) == 1:
            if Play1[0] > Play2[0]:
                draw_text("Round "+str(roundnum)+" Winner", font, Black, 380, 160)
                pygame.display.update()
                pygame.time.delay(2000)
                Player1.append(Play1[0])
                Player1.append(Play2[0])
                if len(Discard) > 0:
                    for x3 in range(0,len(Discard)):
                        Player1.append(Discard[0])
                        Discard.remove(Discard[0])
                roundnum += 1
                round_start = True

            if Play1[0] < Play2[0]:
                draw_text("Round "+str(roundnum)+" Winner", font, Black, 380, 380)
                pygame.display.update()
                pygame.time.delay(2000)
                Player2.append(Play1[0])
                Player2.append(Play2[0])
                if len(Discard) > 0:
                    for x3 in range(0,len(Discard)):
                        Player1.append(Discard[0])
                        Discard.remove(Discard[0])
                roundnum += 1
                round_start = True
            
            if Play1[0] > 0 and Play2[0] > 0:
                if Play1[0] == Play2[0]:
                    draw_text("WAR TIME!", wartime_font, Red, 120, 160)
                    pygame.display.update()
                    pygame.time.delay(2000)
                    pygame.display.update()
                    Discard.append(Play1[0])
                    Discard.append(Play2[0])
                    Discard.append(Player1[0])
                    Discard.append(Player2[0])
                    Player1.remove(Player1[0])
                    Player2.remove(Player2[0])
                    roundnum += 1
                    round_start = True
            Play1.remove(Play1[0])
            Play2.remove(Play2[0])
            screen.blit(pygame.transform.scale(bg_img,(screen_width,screen_height)), (0,0))

    return Shuffled, round_start, roundnum


#creating lists for Player decks and play deck
Game_deck = []
Player1 = []
Player2 = []
Play1 = []
Play2 = []
Discard = []

#creates the card deck
for x in range(1,13):
    for z in range(0,5):
        Game_deck.append(x)
Game_deck.append(13)
Game_deck.append(13)

#creating buttons and giving coordinates to place them on the window and an image to display
#btn = button
Singleplayer_btn = MenuButton(340, 220, singleplayer_img)
Multiplayer_btn = MenuButton(340, 345, multiplayer_img)
Rules_btn = MenuButton(345, 470, rules_img)
Continue_btn = MenuButton(330, 450, continue_img)
Card_btn1 = MenuButton(75, 75, Card_back_img)
Card_btn2 = MenuButton(75, 350, Card_back_img)
Card_btn3 = MenuButton(775, 75, Card_back_img)
Card_btn4 = MenuButton(775, 350, Card_back_img)

#starts the main game loop
run = True
clicked = False
round_start = True
roundnum = 1
Shuffled = False

while run == True:
    #runs this if statement if the gameplay variable is 0 (start of program or game over)
    if Gameplay == 0:
        #prints the background first before the other images so there is no overlap
        screen.blit(pygame.transform.scale(bg_img,(screen_width,screen_height)), (0,0))
        screen.blit(pygame.transform.scale(title_img,(250,125)), (370,30))

        #sets the main menu and instructions variable to true to make them reappear
        main_menu = True
        instructions = True

    #runs this if statement if the gameplay variable is 1 (player selected singleplayer mode)
    elif Gameplay == 1:

        #starts the singleplayer function which is the singleplayer gamemode against a "bot"
        if Shuffled == False:
            
            Shuffle_deck()
            Shuffled = True
                
        if len(Player2) != 52 or len(Player2) != 52 or roundnum <= 200:
                    
                if round_start == True:
                    round_start = Round_countdown(round_start)
                    round_start = False
                                    
                if len(Play1) != 1 and len(Play2) != 1:
                   Handle_key_presses(clicked)

                if len(Play1) == 1 and len(Play2) == 1:
                    Handle_war_round(roundnum)
                
    #runs this if statement if the gameplay variable is 2 (player selected multiplayer mode)
    elif Gameplay == 2:
        
        #starts the multiplayer function which is the multiplayer game mode against another person
        Shuffled, round_start, roundnum = Multiplayer(round_start, clicked, Shuffled, roundnum)


                
    #runs the section if the main menu variable is true
    if main_menu == True:

        
        Card_btn1.draw(Ace_img, Card_back_img)
        Card_btn2.draw(Seven_img, Card_back_img)
        Card_btn3.draw(King_img, Card_back_img)
        Card_btn4.draw(Jack_img, Card_back_img)
        

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

        if Rules_btn.draw(rules_img_hover, rules_img):

            #sets the main menu variable to false(stops the main menu screen loop)
            instructions = False

            #sets the Gameplay variable to 2 (multiplayer game)
            Gameplay = 0

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