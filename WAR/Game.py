# Owen Covach, Katarina Lukic, Yilin Xu
# Module 14 Final Project "WAR"

#importing pygame into the program
import pygame
# asterisk means import all
from pygame.locals import *
import random

#initiates pygame and the fonts
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
# In this case the title is WAR
pygame.display.set_caption('WAR!')

#setting a variable to check if the program is in the main menu or not
main_menu = True

#setting a variable to check if the user clicked singleplayer, multiplayer or if the game has ended
Gameplay = 0
clicked = False
round_start = True
Shuffled = False

#creating a font for all  text in the game (font style, font size) 
font = pygame.font.SysFont('impact', 36)
wartime_font = pygame.font.SysFont('impact', 200)
Countdown_font = pygame.font.SysFont('comicsans', 50)

#defining the colours for the main menu White, Black, Yellow, Blue(uses RGB values to make colours)
#RGB is how much of either Red, Blue or Green a colour has, the higher the number the higher the saturation
White = (255,255,255)
Black = (0,0,0)
Yellow = (255,255,0)
Blue = (0,0,255)
Green = (0,255,0)
Red = (255,0,0)

#setting variables as images to use for the title, single player or mulitplayer(convert_alpha is a function that helps make the game run smoother)
#'pygame.image.load' loads an image from a directory in your computer
# it can load an image from a folder, and in this case the folder is called "assets"
#'pygame.transform.scale' scales the image to the desired resolution specified
play_bg_img = pygame.image.load('Assets/WAR_bg.jpg').convert_alpha()
menu_bg_img = pygame.image.load('Assets/mainmenu.png').convert_alpha()
title_img = pygame.image.load('Assets/WAR_title.png').convert_alpha()
singleplayer_img = pygame.image.load('Assets/start_btn.png').convert_alpha()
singleplayer_img_hover = pygame.image.load('Assets/start_btn_hover.png').convert_alpha()
multiplayer_img = pygame.image.load('Assets/start_btn2.png').convert_alpha()
multiplayer_img_hover = pygame.image.load('Assets/start_btn2_hover.png').convert_alpha()
rules_img = pygame.image.load('Assets/rules_btn.png').convert_alpha()
rules_img_hover = pygame.image.load('Assets/rules_btn_hover.png').convert_alpha()
continue_img = pygame.image.load('Assets/continue_btn.png').convert_alpha()
continue_img_hover = pygame.image.load('Assets/continue_btn_hover.png').convert_alpha()
MainMenu_img = pygame.image.load('Assets/MainMenu_btn.png').convert_alpha()
MainMenu_img_hover = pygame.image.load('Assets/MainMenu_btn_hover.png').convert_alpha()
MainMenu_img = pygame.transform.scale(MainMenu_img,(309,103)).convert_alpha()
MainMenu_img_hover = pygame.transform.scale(MainMenu_img_hover,(309,103)).convert_alpha()
Card_back_img = pygame.image.load('Assets/BACK.png').convert_alpha()
Card_back_img = pygame.transform.scale(Card_back_img,(150, 200))
War_pile_img = pygame.image.load('Assets/War_pile.png').convert_alpha()
Ace_img =  pygame.image.load('Assets/1CARD.png').convert_alpha()
Ace_img = pygame.transform.scale(Ace_img,(150, 200))
Seven_img =  pygame.image.load('Assets/7CARD.png').convert_alpha()
Seven_img = pygame.transform.scale(Seven_img,(150, 200))
King_img =  pygame.image.load('Assets/13CARD.png').convert_alpha()
King_img = pygame.transform.scale(King_img,(150, 200))
Jack_img =  pygame.image.load('Assets/11CARD.png').convert_alpha()
Jack_img = pygame.transform.scale(Jack_img,(150, 200))

#defining a function named draw_text that draws the text and font on the coordinate plane 
def draw_text(text, font, text_col, x, y,):    
    
    #setting a variable as the text that is given and renders is with a given colour
    img = font.render(text, True, text_col)

    #draws the text on the display window
    screen.blit(img, (x, y))
    
#creates a class for the button in regards to the location, size and if it is clicked or not
class MenuButton():

    #this function is the creation of the button itself, it's called when the class is called
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
   
    #this function checks for cursor collision as well as draws the button onto the window
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
        
        #if mouse if not over button, it will then set the image to the original button image unaltered
        else:
            self.image = image2        

        #checks if the mouse isn't pressed
        if pygame.mouse.get_pressed()[0] == 0:
            #sets the click variable as false so the computer knows its not pressed
            self.clicked = False
        

        #drawing the button
        screen.blit(self.image, self.rect)

        #returns the value of action
        return action

#this function is called when the countdown happens before each card flip
def Round_countdown(Gameplay):
    
    #defining a function named Game_overlay
    def Game_overlay():
        #draws overlay of the gameplay screen
        screen.blit(pygame.transform.scale(play_bg_img,(screen_width,screen_height)), (0,0))
        screen.blit(MainMenu_img, (20,475))
        # draws the text including the round number and the font of the countdown
        draw_text("Round "+str(roundnum), Countdown_font, White, 40, 20)
        # draws the text including the player 1 cards and the font
        draw_text('Player 1 Cards: ' +str(len(Player1_deck)), font, Black, 380, 40)

        #this will only draw if the user chose singleplayer ( 1 player vs a bot)
        if Gameplay == 1:
            # draws the text for the computer cards including the font
            draw_text('Computer Cards: ' +str(len(Player2_deck)), font, Black, 360, 540)
    
        #this will only draw if the user chose multiplayer ( 2 players on the same device)
        elif Gameplay == 2:
            # draws the text for the 2nd player cards including the font
            draw_text('Player 2 Cards: ' +str(len(Player2_deck)), font, Black, 380, 540)

        #this will only draw if the user chose multiplayer
        if Gameplay == 2:
            # draws the text for the controls on how to flip a card and their positioning
            draw_text("Press L to flip", font, White, 695, 540)
        draw_text("Press A to flip", font, White, 695, 40)

        #draws the discard pile outline on the left of the screen
        screen.blit(pygame.transform.scale(War_pile_img,(150, 200)), (150,200))

        #draws the player's decks on the right of the screen
        screen.blit(pygame.transform.scale(Card_back_img,(150, 200)), (700,70))
        screen.blit(pygame.transform.scale(Card_back_img,(150, 200)), (700,332))

        #will only draw if the war pile has cards because the 2 players are at war
        if len(War_pile) > 0:
            screen.blit(pygame.transform.scale(Card_back_img,(150, 200)), (150,220))

    #runs the overlay function
    Game_overlay()
    screen.blit(MainMenu_img, (20,475))
    #displays the countdown of 3 seconds onto the screen
    draw_text("3", Countdown_font, White, 440, 240)
    
    #'pygame.display.update' updates the screen so the user sees the changes to the window
    pygame.display.update()
    
    #'pygame.time.delay' delays the code for desired amount of milliseconds (1000 mlliseconds in this case)
    pygame.time.delay(1000)
    
    Game_overlay()
    screen.blit(MainMenu_img, (20,475))
    # draws the text again but for the number 2 instead of 3 to countdown
    draw_text("2", Countdown_font, White, 480, 240)
    
    #updates the display to now dispay a 2 instead of a 3
    pygame.display.update()
    
    # again delays the number from displaying for 1000 milliseconds (as in a real countdown)
    pygame.time.delay(1000)
    
    Game_overlay()
    
    # draws the text again but for the number 1 instead of 2 to countdown
    draw_text("1", Countdown_font, White, 520, 240)
    
    #updates the display to now dispay a 1 instead of a 2
    pygame.display.update()
    
    # again delays the number from displaying for 1000 milliseconds (as in a real countdown)
    pygame.time.delay(1000)
    
    Game_overlay()
    screen.blit(MainMenu_img, (20,475))
    # draws the text again but for the word "FLIP!" instead of the countdown
    draw_text("FLIP!", Countdown_font, White, 435, 290)
    
    #updates the display to now dispay a "FLIP! instead of the countdown
    pygame.display.update()
    
     # again delays the number from displaying for 1000 milliseconds (as in a real countdown)
    pygame.time.delay(1000)

    #draws the overlay again
    Game_overlay()
    screen.blit(MainMenu_img, (20,475))
    #will play the bot's card if the user chose singleplayer
    if Gameplay == 1:

        #runs a loop to go through all the 13 card values and only displays the card's value,
        #(eg. if Player2_deck[0] =  6, "Player2_deck[0] == x1" is only true when x1 is 6 in this case so it only displays the 6 card onto the screen)
        for x1 in range(0,14):
            if Player2_deck[0] == x1:
                #draws the card onto screen using images from the assets folder
                screen.blit(pygame.transform.scale(pygame.image.load('Assets/'+str(x1)+'CARD.png'),(150, 200)), (420,320))
    pygame.display.update()
    
#defines a function named Shuffle_deck
def Shuffle_deck():
    #shuffles then deals deck

        #what this does is go through each index in the game deck, and swaps it with a random number in the deck from the range of 'x' to the end of the list
        #goes through each value from the list
        for x in range(0,52):

            #generates a random number from x to the end of the list
            rand = random.randint(x,51)
                                    
            #sets a temporary value as the game deck value of index 'x'
            temp = Game_deck[x]

            #then sets the game deck value at index 'x' to the game deck value at index 'rand' (a random number)
            Game_deck[x] = Game_deck[rand]

            #then sets the game deck value at index 'rand' to the temp value which was the original game deck value at index 'x'
            Game_deck[rand] = temp
                                
        #deals the deck by giving player1 evens and player2 odds (dealing 1 by 1)
        for x in range(0,26):
            #append command adds the given value to the end of the list
            Player1_deck.append(Game_deck[2 * x])
            Player2_deck.append(Game_deck[2 * x + 1])

#defines a function named Handle-key-presses that has clicked and Gameplay passed through it
def Handle_key_presses(clicked, Gameplay):
    
    #runs the singleplayer button presses
    if Gameplay == 1:

        #scans for any key presses constantly
        keys_pressed = pygame.key.get_pressed()

        #checks if the 'A' key was pressed, if it hasnt been clicked already, and if there isn't a card already flipped
        if keys_pressed[pygame.K_a] and clicked == False and len(Flipped_pile1) == 0:
      
            #runs a loop to go through all the 13 card values and only displays the card's value,
            for x1 in range(1,14):
                if Player1_deck[0] == x1:
                    #draws the card onto screen
                    screen.blit(pygame.transform.scale(pygame.image.load('Assets/'+str(x1)+'CARD.png'),(150, 200)), (420,90))
                    #updates the display window
                    pygame.display.update()

            #moves the top card from each player's deck onto the flipped card piles (put each player card in play)
            Flipped_pile1.append(Player1_deck[0])
            #'.remove' is called, so that when a card from a deck is added to another deck, 
            #it's deleted from the original deck so that there aren't endless amount of cards
            Player1_deck.remove(Player1_deck[0])
            Flipped_pile2.append(Player2_deck[0])
            Player2_deck.remove(Player2_deck[0])

            #sets clicked to True to stop instantly placing another card
            clicked = True
        
        #checks if user lets go of 'A' key
        elif keys_pressed[pygame.K_a]:

            #sets clicked to False so the user can play another card next round when it is their turn
            clicked = False
    
    #runs the multiplayer button presses
    if Gameplay == 2:
        #scans for any key presses constantly
        keys_pressed = pygame.key.get_pressed()

        #checks if the 'A' key was pressed, if it hasnt been clicked already, and if there isntt a card already flipped
        if keys_pressed[pygame.K_a] and clicked == False and len(Flipped_pile1) == 0:

            #runs a loop to go through all 13 values and only displays the card's value
            for x1 in range(1,14):
                if Player1_deck[0] == x1:

                    #draws the card onto screen
                    screen.blit(pygame.transform.scale(pygame.image.load('Assets/'+str(x1)+'CARD.png'),(150, 200)), (420,90))
                    pygame.display.update()

            #moves the top card from player1's deck onto the flipped card pile (puts player1's card in play)
            #'.remove' is called, so that when a card from a deck is added to another deck, it's deleted from the original deck
            # so that there aren't endless amount of cards
            Flipped_pile1.append(Player1_deck[0])
            Player1_deck.remove(Player1_deck[0])

            #sets clicked to True to stop instantly placing another card
            clicked = True
        
        #checks if the 'L' key was pressed, if it hasnt been clicked already, and if there isn't a card already flipped
        elif keys_pressed[pygame.K_l] and clicked == False and len(Flipped_pile2) == 0:

            #runs a loop to go through all 13 values and only displays the card's value
            for x2 in range(1,14):
                if Player2_deck[0] == x2:

                    #draws the card onto screen
                    screen.blit(pygame.transform.scale(pygame.image.load('Assets/'+str(x2)+'CARD.png'),(150, 200)), (420,320))
                    pygame.display.update()

            #moves the top card from player2's deck onto the flipped card pile (puts player2's card in play)
            #'.remove' is called, so that when a card from a deck is added to another deck, its deleted from the original deck
            # so that there aren't endless amount of cards
            Flipped_pile2.append(Player2_deck[0])
            Player2_deck.remove(Player2_deck[0])

            #sets clicked to True to stop instantly placing another card
            clicked = True
            
        #checks if players let go of 'A' or 'L' key
        elif keys_pressed[pygame.K_a] == False or keys_pressed[pygame.K_l] == False:

            #sets clicked to False so the user can play another card next round when it is their turn
            clicked = False

#defines a function named Handle_calculations which handles all the calculations
def Handle_calculations(roundnum, round_start):

    #checks if Player1 has higher card value than Player 2 from their flipped piles
    if Flipped_pile1[0] > Flipped_pile2[0]:

        #draws the round winner text on screen on top of the card that won, which shows for 2 seconds
        draw_text("Round "+str(roundnum)+" Winner", font, Green, 380, 160)
        #updates the display window so it can now show the winner for the round
        pygame.display.update()
        # this shows up for 2000 miliiseconds so the user can read it before it disapears
        pygame.time.delay(2000)

        #adds the cards to Player 1's deck from Player 2
        Player1_deck.append(Flipped_pile1[0])
        Player1_deck.append(Flipped_pile2[0])

        #checks if there were any cards in the war pile to add
        if len(War_pile) > 0:
            
            #adds all cards from the war pile to Player1's deck
            for x3 in range(0,len(War_pile)):
                Player1_deck.append(War_pile[0])
                #removes the cards from the war pile
                War_pile.remove(War_pile[0])
        
        #add 1 to roundnum to count up the amount of rounds
        #sets round_start to True to run the countdown again
        roundnum += 1
        round_start = True

    #checks if Player1 has lower card value than Player 2
    if Flipped_pile1[0] < Flipped_pile2[0]:

        #draws the round winner text on screen ontop of the card that won, which shows for 2 seconds
        draw_text("Round "+str(roundnum)+" Winner", font, Green, 380, 380)
        pygame.display.update()
        pygame.time.delay(2000)

        #adds the cards to Player2's deck from Player 1
        Player2_deck.append(Flipped_pile1[0])
        Player2_deck.append(Flipped_pile2[0])

         #checks if there were any cards in the war pile to add
        if len(War_pile) > 0:
            for x3 in range(0,len(War_pile)):

                #adds all cards from the war pile to Player 2's deck
                Player2_deck.append(War_pile[0])
                War_pile.remove(War_pile[0])

        #add 1 to roundnum to count up the amount of rounds
        #sets round_start to True to run the countdown again
        roundnum += 1
        round_start = True
    
    #checks if Player1 has same value as Player 2 ( if the same then they go to war!)
    if Flipped_pile1[0] == Flipped_pile2[0]:

        #draws text in the middle of the screen, which shows for 2 seconds
        draw_text("WAR TIME!", wartime_font, Red, 140, 160)
        # updates the display to show the text war time
        pygame.display.update()
        pygame.time.delay(2000)

        #adds both the flipped cards and adds the top card from each player's deck for a total of 4 in the war pile
        War_pile.append(Flipped_pile1[0])
        War_pile.append(Flipped_pile2[0])
        War_pile.append(Player1_deck[0])
        War_pile.append(Player2_deck[0])
        #'.remove' is called, so that when a card from a deck is added to another deck, 
        #its deleted from the original deck so that there aren't infite cards
        Player1_deck.remove(Player1_deck[0])
        Player2_deck.remove(Player2_deck[0])

        #add 1 to roundnum to count up the amount of rounds
        #sets round_start to True to run the countdown again
        roundnum += 1
        round_start = True
    Flipped_pile1.remove(Flipped_pile1[0])
    Flipped_pile2.remove(Flipped_pile2[0])
    # returns these values
    return round_start, roundnum

#defines a function named Intructions which handles the instructions window
def Instructions(Gameplay, main_menu):
    
    if Continue_btn.draw(continue_img_hover, continue_img):
        Gameplay = 0
        main_menu = False

    return Gameplay, main_menu

#creating lists for Player decks and the flipped pile
Game_deck = []
War_pile = []
Flipped_pile1 = []
Flipped_pile2 = []

#creates the card deck
# the 1st for loop is for the 13 different types of cards ( ace, 2-10, jack, queen, king)
for x in range(1,14):
    # the 2nd for loop is for the 4 suits (club, spades, hearts, diamonds)
    for z in range(0,4):
        Game_deck.append(x)

#creating buttons and giving coordinates to place them on the window and an image to display
#btn = button
Singleplayer_btn = MenuButton(340, 220, singleplayer_img)
Multiplayer_btn = MenuButton(340, 345, multiplayer_img)
Rules_btn = MenuButton(345, 470, rules_img)
Continue_btn = MenuButton(345, 475, continue_img)
MainMenu_btn = MenuButton(20,475, MainMenu_img)
Card_btn1 = MenuButton(75, 75, Card_back_img)
Card_btn2 = MenuButton(75, 350, Card_back_img)
Card_btn3 = MenuButton(775, 75, Card_back_img)
Card_btn4 = MenuButton(775, 350, Card_back_img)

run = True
while run == True:
    
    #runs this if statement if the gameplay variable is 0 (start of program or if a player wins)
    if Gameplay == 0:
        #prints the background first before the other images so there is no overlap then the title image
        screen.blit(pygame.transform.scale(menu_bg_img,(screen_width,screen_height)), (0,0))
        screen.blit(pygame.transform.scale(title_img,(400,130)), (310,40))

        #sets the main menu and instructions variable to true to run the main menu again and load instructions if the rules button is pressed
        main_menu = True
        Shuffled = False
        roundnum = 98
        clicked = False
        round_start = True

    #runs this if statement if the gameplay variable is 1 (player selected singleplayer mode)
    elif Gameplay == 1:
        if MainMenu_btn.draw(MainMenu_img_hover, MainMenu_img):
            Gameplay = 0
        #starts the singleplayer function which is the singleplayer gamemode against a "bot"
        if Shuffled == False:

            #creates the player decks
            Player1_deck = []
            Player2_deck = []

            #runs the Shuffle_deck function
            Shuffle_deck()

            #sets the shuffeld variable to true so it doesnt shuffle again
            Shuffled = True

        #checks if 100 rounds have passed so the game doesn't go on forever
        if roundnum < 101:    

            #checks if a player has 52 cards in their possesion
            if len(Player2_deck) != 52 or len(Player2_deck) != 52:
                    
                    #checks if a new round has begun
                    if round_start == True:
                        #runs the Round_countdown function, displays a countdown for users
                        Round_countdown(Gameplay)
                        #stops the countdown from the loop
                        round_start = False

                    #checks if both players haven't flipped their card
                    if len(Flipped_pile1) == 0 and len(Flipped_pile2) == 0 or len(Flipped_pile1) == 1 and len(Flipped_pile2) == 0 or len(Flipped_pile1) == 0 and len(Flipped_pile2) == 1:
                        #runs the Handle_key_presses function, constantly checks for button presses to flip cards
                        Handle_key_presses(clicked, Gameplay)
                    
                    #checks if both players flipped their cards
                    if len(Flipped_pile1) == 1 and len(Flipped_pile2) == 1:
                        #runs the Handle_calculations function to check who won the round
                        # sets round_start and roundnum values so the variable can get updated to keep working properly
                        round_start, roundnum = Handle_calculations(roundnum, round_start)
        
        #if round 100 was complete, it ends the game and brings you back to main menu
        else:

            #draws the background to erase overlay
            screen.blit(pygame.transform.scale(play_bg_img,(screen_width,screen_height)), (0,0))

            #draws game end text with the winner ( player 1 or computer)
            draw_text("Game End", wartime_font, Red, 110, 120)
            if Player1_deck > Player2_deck:
                draw_text("Player 1 Won!", font, Green, 380, 350)
            if Player1_deck < Player2_deck:
                draw_text("Computer Won!", font, Green, 380, 350)
            pygame.display.update()
            pygame.time.delay(5000)

            #sets Gameplay value to 0, which sends user to main menu
            Gameplay = 0
        
    #runs this if statement if the gameplay variable is 2 (player selected multiplayer mode)
    elif Gameplay == 2:
        if MainMenu_btn.draw(MainMenu_img_hover, MainMenu_img):
            Gameplay = 0
        #starts the singleplayer function which is the singleplayer gamemode against a "bot"
        if Shuffled == False:
            #creates the player decks
            Player1_deck = []
            Player2_deck = []

            #runs the Shuffle_deck function
            Shuffle_deck()

            #sets the shuffeld variable to true so it doesnt shuffle again
            Shuffled = True

        #checks if 100 rounds have passed so the game doesn't go on forever
        if roundnum < 101:    

            #checks if a player has 52 cards
            if len(Player2_deck) != 52 or len(Player2_deck) != 52:
                    
                    #checks if a new round has begun
                    if round_start == True:
                        #runs the Round_countdown function, displays a countdown for users
                        Round_countdown(Gameplay)
                        #stops the countdown from the loop
                        round_start = False

                    #checks if both players haven't flipped their card
                    if len(Flipped_pile1) == 0 and len(Flipped_pile2) == 0 or len(Flipped_pile1) == 1 and len(Flipped_pile2) == 0 or len(Flipped_pile1) == 0 and len(Flipped_pile2) == 1:
                        #runs the Handle_key_presses function, constantly checks for button presses to flip cards
                        Handle_key_presses(clicked, Gameplay)
                    
                    #checks if both players flipped their cards
                    if len(Flipped_pile1) == 1 and len(Flipped_pile2) == 1:
                        #runs the Handle_calculations function to check who won the round
                        # sets round_start and roundnum values so the variable get updated to keep working properly
                        round_start, roundnum = Handle_calculations(roundnum, round_start)

        #if round 100 was complete, it ends the game and brings you back to main menu
        else:

            #draws the background to erase overlay
            screen.blit(pygame.transform.scale(play_bg_img,(screen_width,screen_height)), (0,0))

            #draws game end text with the winner (Player 1 or 2)
            draw_text("Game End", wartime_font, Red, 150, 140)
            if Player1_deck > Player2_deck:
                draw_text("Player 1 Won!", font, Green, 420, 370)
            if Player1_deck < Player2_deck:
                draw_text("Player 2 Won!", font, Green, 420, 370)
            pygame.display.update()
            pygame.time.delay(5000)

            #sets Gameplay value to 0, which sends user to the main menu
            Gameplay = 0

    elif Gameplay == 3:
                Gameplay, main_menu = Instructions(Gameplay, main_menu)    
            
    #runs the section if the main menu variable is true
    if main_menu == True:

        #drawing card backs as a small menu feature, flips the card when hovered over
        Card_btn1.draw(Ace_img, Card_back_img)
        Card_btn2.draw(Seven_img, Card_back_img)
        Card_btn3.draw(King_img, Card_back_img)
        Card_btn4.draw(Jack_img, Card_back_img)

        #checks if the singleplayer button was pressed
        if Singleplayer_btn.draw(singleplayer_img_hover, singleplayer_img):
            
            #sets the main menu variable to false (stops the main menu screen loop)
            main_menu = False

            #sets the Gameplay variable to 1 (singleplayer game)
            Gameplay = 1

            #delays button reaction by 100 milliseconds
            pygame.time.delay(100)

            #draws the background image to remove the menu images
            screen.blit(pygame.transform.scale(play_bg_img,(screen_width,screen_height)), (0,0))

        #checks if the multiplayer button was pressed
        if Multiplayer_btn.draw(multiplayer_img_hover, multiplayer_img):

            #sets the main menu variable to false(stops the main menu screen loop)
            main_menu = False

            #sets the Gameplay variable to 2 (multiplayer game)
            Gameplay = 2

            #delays button reaction by 100 milliseconds
            pygame.time.delay(100)

            #draws that background image to remove menu images
            screen.blit(pygame.transform.scale(play_bg_img,(screen_width,screen_height)), (0,0))

        if Rules_btn.draw(rules_img_hover, rules_img):
            
            screen.blit(pygame.transform.scale(menu_bg_img,(screen_width,screen_height)), (0,0))
            draw_text("How to play:", Countdown_font, White, 360, 20)
            draw_text("Each Players has 26 cards each", font, White, 310, 105)
            draw_text("Player 1 flips a card over with the 'A' key", font, White, 270, 130)
            draw_text("Player 2 flips a card over with the 'L' key", font, White, 270, 155)
            draw_text("Once each player flips a card,", font, White, 325, 180)
            draw_text("Highest card value wins the round", font, White, 300, 205)
            draw_text("The winner gets the played cards,", font, White, 300, 230)
            draw_text("If cards are the same value, 'WAR' begins:", font, White, 260, 255)
            draw_text("The cards played and 1 card from each player's deck", font, White, 195, 280)
            draw_text("Gets added to the war pile for the next round", font, White, 245, 305)
            draw_text("When a player wins following a 'WAR'", font, White, 275, 330)
            draw_text("The winner gets the played cards,", font, White, 300, 355)
            draw_text("Additionally the winner gets the war pile", font, White, 260, 380)
            draw_text("if a player reaches 52 cards, they win", font, White, 285, 405)
            draw_text("if 100 rounds passed, player with the most cards wins", font, White, 190, 430)
            

            # updates the display to show the instruction text
            pygame.display.update()

            #sets the main menu variable to false(stops the main menu screen loop)
            Gameplay = 3
            main_menu = False

            #delays button reaction by 100 milliseconds
            pygame.time.delay(100)
            
    # if the player has quit the game then the program will close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #sets a framerate for the computer to run at
    clock.tick(fps)

    #updates the pygame display after each user input
    pygame.display.update()
       
# closes the pygame application
pygame.quit()
