import pygame # importing the package.
pygame.init() # importing all the func that in the pack.
import time # importig the time package.
import random #importing the random package.

crash_sound = pygame.mixer.Sound(r"C:\Users\Avi Fenesh\OneDrive\שולחן העבודה\python\Crash.wav") #importing crash sound
backruond_sound = pygame.mixer.music.load(r"C:\Users\Avi Fenesh\OneDrive\שולחן העבודה\python\Butchers.wav") #importing backruond sound


display_width = 800
display_height = 600

black = (0, 0, 0) # def variable for color - black.
white = (255, 255, 255) # def variable for color - white.
red = (200, 0 ,0)
green = (0, 200, 0)
blue = (0, 0, 255)
bright_red = (255, 0 ,0)
bright_green = (0, 255, 0)

block_colors = ((140, 85, 180), (127, 210, 194), (59, 210, 83), (225, 167, 83), (118, 189, 117), (234, 189, 117), (234, 135, 86), red, blue, green,bright_green, bright_red) # def a tuple of colors that we gonna use for the block.

car_width = 73 # the width of the car img.

game_over = False

pause = False #for pause func

with open(r"C:\Users\Avi Fenesh\OneDrive\שולחן העבודה\python\pygame\score.txt", "r") as best_score_file:
    best_score = best_score_file.read() # checking the best score.


GameDisplay = pygame.display.set_mode((display_width, display_height)) # set the size of the window for the program.
pygame.display.set_caption("A bit Racy") # set the name for the program.
clock = pygame.time.Clock() # set the clock for the program.

carImg = pygame.image.load(r"C:\Users\Avi Fenesh\OneDrive\שולחן העבודה\python\pygame\racecar.png") # loading the img of the car.
carIcon = pygame.image.load(r"C:\Users\Avi Fenesh\OneDrive\שולחן העבודה\python\pygame\racecar4.png") # loading the img of the car.
pygame.display.set_icon(carIcon) # set icon for the prog.

def quit_game():
    pygame.quit()
    quit()

def things_dodged(count): # counting the screen that the player survived, and prunting it on the screen.
    font = pygame.font.SysFont('comicsansms', 25)
    text = font.render("Dodged: "+str(count), True, black)
    GameDisplay.blit(text,(0,0))

def things(list_thingx, thingy, thingw, thingh, color): # def the things that gonna show on the screen that we want to avoid with our img.
    for thing in list_thingx:
        pygame.draw.rect(GameDisplay, color, [thing, thingy, thingw, thingh])  # Draw those thing

def car(x, y):
    # printing the car img where we want it.
    GameDisplay.blit(carImg, (x,y))

def text_object(text, font): # def the variable that we gonna give for a text the while we calling message_display, that calling this func.
    TextSurFace = font.render(text, True, black) # def the variable that we gonna give to the blit func for the text itself.
    return  TextSurFace, TextSurFace.get_rect() # def what we gonna give for the blit func, text and rect.

def message_display(text): # def displaying of text on the surface when we call this func
    LargeText = pygame.font.SysFont('comicsansms', 115) # def the font of the text that will display.
    TextSurf, TextRect = text_object(text, LargeText) # def variable for tuple that we will give to blit func, that gonna print it on the surface. text_object call another func that use the variable that we gave, and give back all the right variable for calling blit.
    TextRect.center = ((display_width / 2), (display_height / 2)) # def where on the surface the text gonna show. here its define it on the middle
    GameDisplay.blit(TextSurf, TextRect) # showing the text on the screen.
    pygame.display.update() # update the game with the func.
    time.sleep(2) # def how long this func are gona be.
    game_loop() # caliing new loop after the func (the text showing) will end.



def crash(): # def what will happen wile crash, and a try again screen.
    pygame.mixer.music.stop() #stop the backround music.
    pygame.mixer.Sound.play(crash_sound) # play crash sound
    global game_over
    game_over = True

    LargeText = pygame.font.SysFont('comicsansms', 115)  # def the font of the text that will display.
    TextSurf, TextRect = text_object("You crashed!", LargeText)  # def variable for tuple that we will give to blit func, that gonna print it on the surface. text_object call another func that use the variable that we gave, and give back all the right variable for calling blit.
    TextRect.center = ((display_width / 2), (display_height / 2))  # def where on the surface the text gonna show. here its define it on the middle
    GameDisplay.blit(TextSurf, TextRect)  # showing the text on the screen.

    with open(r"C:\Users\Avi Fenesh\OneDrive\שולחן העבודה\python\pygame\score.txt", "r") as best_score_file:
        best_score = best_score_file.read()  # checking the best score.

    smallText = pygame.font.SysFont('candara', 40)  # def the font of the text that will display.
    string_to_print = "best score: " + str(best_score)
    TextSurf, TextRect = text_object(string_to_print, smallText)  # def variable for tuple that we will give to blit func, that gonna print it on the surface. text_object call another func that use the variable that we gave, and give back all the right variable for calling blit.
    TextRect.center = ((400), (550))  # def where on the surface the text gonna show. here its define it on the middle
    GameDisplay.blit(TextSurf, TextRect)

    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #GameDisplay.fill(white)
        button("Try again", 180, 400, 130, 50, green, bright_green, game_loop) # def button continue
        button("Quit", 480, 400, 130, 50, red, bright_red, quit_game) # def button quit
        # draw black lines for the buttons.
        pygame.draw.line(GameDisplay, black, (180, 400), (310, 400), 3)
        pygame.draw.line(GameDisplay, black, (180, 450), (310, 450), 3)
        pygame.draw.line(GameDisplay, black, (180, 400), (180, 450), 3)
        pygame.draw.line(GameDisplay, black, (310, 400), (310, 450), 3)
        pygame.draw.line(GameDisplay, black, (480, 400), (610, 400), 3)
        pygame.draw.line(GameDisplay, black, (480, 450), (610, 450), 3)
        pygame.draw.line(GameDisplay, black, (480, 400), (480, 450), 3)
        pygame.draw.line(GameDisplay, black, (610, 400), (610, 450), 3)

        pygame.display.update()
        clock.tick(15)


def button(msg, x, y, w, h, ic, ac, action = None): #def func for the button in the game.
    mouse = pygame.mouse.get_pos()  # save variable for the mouse
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:  # def what will happend when the mouse touch the button.
        pygame.draw.rect(GameDisplay, ac, (x, y, w, h))  # draw the bright  button.
        if click[0] == 1 and action != None :
            action() # def what will happen if click the button.
    else:
        pygame.draw.rect(GameDisplay, ic, (x, y, w, h))  # draw the button.
    # printing a text on the button -
    small_text = pygame.font.SysFont('comicsansms', 25)
    textSurf, textRect = text_object(msg, small_text)
    textRect.center = ((x + (w / 2)), (y + h / 2))
    GameDisplay.blit(textSurf, textRect)

def unpaused(): # def func for unpaused, after pause func.
    global pause
    pause = False
    pygame.mixer.music.unpause() #unpause the music.

def paused(): # def a pause to the game.
    global pause
    pygame.mixer.music.pause() # pause the music while pause.
    LargeText = pygame.font.SysFont('comicsansms', 115)  # def the font of the text that will display.
    TextSurf, TextRect = text_object("Paused", LargeText)  # def variable for tuple that we will give to blit func, that gonna print it on the surface. text_object call another func that use the variable that we gave, and give back all the right variable for calling blit.
    TextRect.center = ((display_width / 2), (
                display_height / 2))  # def where on the surface the text gonna show. here its define it on the middle
    GameDisplay.blit(TextSurf, TextRect)  # showing the text on the screen.

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #GameDisplay.fill(white)
        button("Continue", 180, 400, 130, 50, green, bright_green, unpaused) # def button continue
        button("Quit", 480, 400, 130, 50, red, bright_red, quit_game) # def button quit
        # draw black lines for the buttons.
        pygame.draw.line(GameDisplay, black, (180, 400), (310, 400), 3)
        pygame.draw.line(GameDisplay, black, (180, 450), (310, 450), 3)
        pygame.draw.line(GameDisplay, black, (180, 400), (180, 450), 3)
        pygame.draw.line(GameDisplay, black, (310, 400), (310, 450), 3)
        pygame.draw.line(GameDisplay, black, (480, 400), (610, 400), 3)
        pygame.draw.line(GameDisplay, black, (480, 450), (610, 450), 3)
        pygame.draw.line(GameDisplay, black, (480, 400), (480, 450), 3)
        pygame.draw.line(GameDisplay, black, (610, 400), (610, 450), 3)

        pygame.display.update()
        clock.tick(15)

def game_intro(): # def a game intro screen.
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        GameDisplay.fill(white)

        LargeText = pygame.font.SysFont('comicsansms', 115)  # def the font of the text that will display.
        TextSurf, TextRect = text_object("A Bit Racy", LargeText)  # def variable for tuple that we will give to blit func, that gonna print it on the surface. text_object call another func that use the variable that we gave, and give back all the right variable for calling blit.
        TextRect.center = ((display_width / 2), (display_height / 2))  # def where on the surface the text gonna show. here its define it on the middle
        GameDisplay.blit(TextSurf, TextRect)  # showing the text on the screen.

        button("GO!", 180, 400, 130, 50, green, bright_green, game_loop) # def button go
        button("Quit", 480, 400, 130, 50, red, bright_red, quit_game) # def button quit

        # draw black lines for the buttons.
        pygame.draw.line(GameDisplay, black, (180, 400), (310, 400), 3)
        pygame.draw.line(GameDisplay, black, (180, 450), (310, 450), 3)
        pygame.draw.line(GameDisplay, black, (180, 400), (180, 450), 3)
        pygame.draw.line(GameDisplay, black, (310, 400), (310, 450), 3)
        pygame.draw.line(GameDisplay, black, (480, 400), (610, 400), 3)
        pygame.draw.line(GameDisplay, black, (480, 450), (610, 450), 3)
        pygame.draw.line(GameDisplay, black, (480, 400), (480, 450), 3)
        pygame.draw.line(GameDisplay, black, (610, 400), (610, 450), 3)

        pygame.display.update()
        clock.tick(15)

def game_loop(): # def a loop for the prog.
    pygame.mixer.music.play(-1) # play music for the game.
    x =  (display_width * 0.45) # def the variable for func car, that will set the location of the car on the window.
    y = (display_height * 0.8) # def the variable for func car, that will set the location of the car on the window.

    x_change = 0 # variable that gonna change and use for moving the img on the screen.

    thing_startx = random.randrange(0, display_width - 80) # def where on x the thing gonna show
    list_thingx = [thing_startx]
    thing_starty = -600 # thef whereon y the thing gonna show. a bit above the toop.
    thing_speed = 4 # def how speed the thin gonna move down.
    thing_width = 80 # def the width of the thing.
    thing_height = 80 # def the height of the thing.
    things_count = 1 # def thh num of things that gonna show on the screen.
    rand_color = random.choice(block_colors) # pick a random color from the list of the colors.

    dodged = 0 # will change withe every "thing" that the player gonna survive.
    global best_score

    game_exit = False # set for the game loop, this variable gonna break when he turning to True
    while not game_exit:# this is the loop of the game. while not crashed mean that the opposite then while crashed. and while crashed = False, cause we didnt crash yet. so while crashed not equale True, we still in the loop.
        for event in pygame.event.get(): # taking all the event that the player will do in the game.
            global pause
            if event.type == pygame.QUIT: # CHECING if the event that the player choose to make is quit.
                pygame.quit()  # quit pygame.
                quit()  # quit the prog.
            if event.type == pygame.KEYDOWN:
                # def what gonna happend to img when the player pushdown the left and right button/
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p: # def what will happen while key down "P" (the game will pause).
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                # def what gonna happend when the player stop pushin the left or right button.
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change # moving the img base of x_chang, that changing based on what the player pushed.
            #print(event) # printing all the events that the player choose to do. none relavent, we did that just for understanding.
        GameDisplay.fill(white) # changing the backround to the color we choose, here we choose white.


        things(list_thingx, thing_starty, thing_width, thing_height, rand_color)  # calling the thing func.

        thing_starty += thing_speed # def how speed the thing gonna move.

        car(x, y) # call the func that print the car img where we want. x and y are the varibale the decide where.
        things_dodged(dodged) # calling the func that printing the score.


        if thing_starty > display_height: # def waht gonna happend when the thing gonna disapear.
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width - 80) # def the place that the thing will show again on the x.
            list_thingx = [thing_startx]
            dodged += 1  # changing the score that printing on the surface.
            if int(best_score) <= dodged:
                with open(r"C:\Users\Avi Fenesh\OneDrive\שולחן העבודה\python\pygame\score.txt", "w") as best_score_file:
                    best_score_file.write(str(dodged))  # saving the best score.
            thing_speed += 1 # changing the speed of the thing.
            #thing_width += (dodged * 1.1) # chaning the size of the things every time that we pass a thing. i dont like it.
            rand_color = random.choice(block_colors) # cahnge the color of the block.
            #things_count += 1 # adding another block any two blocs taht the player pass.
            #if things_count > 1: # option to make the game add a new block to the surface every two blocs.
                #list_thingx = []
                #for num in range(0, things_count, 1):
                    #list_thingx.append(random.randrange(0, display_width - 80))


        if x > display_width - car_width or x < 0: # def what gonna happend if our img going out of the surface boundaries.
            crash()

        if y < thing_starty + thing_height: # def what gonna happened if the img cross the thing.
            for thing in list_thingx:
                if x > thing and x < thing + thing_width or x + car_width > thing and x + car_width < thing + thing_width:
                   crash()

        pygame.display.update() # make updating the surface possible.
        clock.tick(60) # set how much frame to prog will make any seacond.

game_intro() # calling the game intro func.
game_loop() # calling the loop of the prog.
pygame.quit() # quit pygame.
quit() # quit the prog.