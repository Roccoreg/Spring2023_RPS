# File created by: Rocco Reginelli

# import libraries

from time import sleep

from random import randint 

import pygame as pg

import os

game_folder = os.path.dirname(__file__)
print(game_folder)

# game settings
WIDTH = 600
HEIGHT = 600
FPS = 30

# define colors
# tuples are immutable - cannot change once created
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# initializes py game, turns it on, light switch

choices0 = ("Rock, Paper, Scissors")
# FFunction that allows CPU to choose
def cpu_randchoice():
    choice = choices0[randint(0,2)].upper()
    print ("computer randomly decides..." + choice)
    return choice     

pg.init()
pg.mixer.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Rock, Paper, Scissors...")
# frames per second
clock = pg.time.Clock()
# Takes image from the folder and creates a varaible with the picture to display it on screen
rock_image = pg.image.load(os.path.join(game_folder, 'rock.jpg')).convert()
rock_image_rect = rock_image.get_rect()
paper_image = pg.image.load(os.path.join(game_folder, 'paper.jpg')).convert()
paper_image_rect = paper_image.get_rect()
scissors_image = pg.image.load(os.path.join(game_folder, 'scissors.jpg')).convert()
scissors_image_rect = scissors_image.get_rect()
# starting position for all choices that player can choose
rock_image_rect.x = 0
paper_image_rect.x = 200
scissors_image_rect.x = 400
player_choice = ""
cpu_choice = ""
running = True

# prints lets play to start the game
print("Let's play:")
# shows choices (Rock Paper Scissors)
print (choices0)
# Sleep for .5 seconds (rest .5 seconds before printing "Click on Rock, Paper, or Scissors")
sleep (.5)
print ("Click on Rock, Paper, or Scissors")

scissors_image = pg.image.load(os.path.join(game_folder, 'scissors.jpg')).convert()
scissors_image_rect = scissors_image.get_rect()
cpu_scissors_image_rect = scissors_image.get_rect()

paper_image = pg.image.load(os.path.join(game_folder, 'paper.jpg')).convert()
paper_image_rect = paper_image.get_rect()
cpu_paper_image_rect = paper_image.get_rect()

rock_image = pg.image.load(os.path.join(game_folder, 'rock.jpg')).convert()
rock_image_rect = rock_image.get_rect()
cpu_rock_image_rect = rock_image.get_rect()

tiegame_image = pg.image.load(os.path.join(game_folder, 'tiegame.jpg')).convert()
tiegame_image_rect = tiegame_image.get_rect()

youlose_image = pg.image.load(os.path.join(game_folder, 'youlose.jpg')).convert()
youlose_image_rect = youlose_image.get_rect()
# tracks image file location and moves it from file to a picture in the game
youwin_image = pg.image.load(os.path.join(game_folder, 'youwin.jpg')).convert()
youwin_image_rect = youwin_image.get_rect()

while running:
    clock.tick(FPS)
    # event is anytime you do anything with the computer
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # Depends what you define as mouse click
        if event.type == pg.MOUSEBUTTONUP:
            print(pg.mouse.get_pos()[0])
            print(pg.mouse.get_pos()[1])
            mouse_coords = pg.mouse.get_pos()
            # if pg.mouse.get_pos()[0] <= my_image_rect.width and pg.mouse.get_pos()[1] < my_image_rect.height:
            #     print("i clicked the rock")
            # else:
            #     print("no rock....")
            # print(rock_image_rect.collidepoint(mouse_coords))
            # if collided then you clicked on the picture
            if  rock_image_rect.collidepoint(mouse_coords):
                print ("you clicked on rock")
                player_choice = "rock"
                cpu_choice = cpu_randchoice()
            # print(paper_image_rect.collidepoint(mouse_coords))
            # if collided then you clicked on the picture
            elif paper_image_rect.collidepoint(mouse_coords):
                print ("you clicked on paper")
                player_choice = "paper"
                cpu_choice = cpu_randchoice()
            # print(scissors_image_rect.collidepoint(mouse_coords))
            # if collided then you clicked on the picture
            elif scissors_image_rect.collidepoint(mouse_coords):
                print ("you clicked on scissors")
                player_choice = "scissors"
                cpu_choice = cpu_randchoice
                # else statement states that if non of the above was completed say this ""
            else:
                print ("Try again, you did not click anything")
           
########## update ###################

############ draw ###################
    screen.fill(BLACK)
# Rock is drawn on the screen

    #Check to see the outcome of the game
    if player_choice == "":
        # shows three choices a player can make
        screen.blit(rock_image, rock_image_rect)
        screen.blit(paper_image, paper_image_rect)
        screen.blit(scissors_image, scissors_image_rect)
        # shows every scenerio for a rock paper scissors game
    if player_choice == "rock" :
        if cpu_choice == "rock" :
            cpu_rock_image_rect.x = 500
            rock_image_rect = 100
            screen.blit(rock_image, rock_image_rect)
            screen.blit(rock_image, cpu_rock_image_rect)
            # screen.blit puts the image on the screen
            screen.blit(tiegame_image, tiegame_image_rect)
            # .x moves the image to where you want to position it on screen
            tiegame_image_rect.x = 300
    if player_choice == "rock" :
        if cpu_choice == "scissors":
            cpu_scissors_image_rect.x = 500
            rock_image_rect.x = 100
            screen.blit(rock_image, rock_image_rect)
            screen.blit(scissors_image, cpu_scissors_image_rect)
            screen.blit (youwin_image, youwin_image_rect)
            youwin_image_rect.x = 300
    if player_choice == "rock" :
        if cpu_choice == "paper":
            cpu_paper_image_rect.x = 500
            rock_image_rect.x = 100
            screen.blit(rock_image, rock_image_rect)
            screen.blit(paper_image, cpu_paper_image_rect)
            screen.blit (youwin_image, youwin_image_rect)
            youwin_image_rect.x = 300
    if player_choice == "scissors" :
        if cpu_choice == "scissors":
            cpu_scissors_image_rect.x = 500
            scissors_image_rect.x = 100
            screen.blit(scissors_image, scissors_image_rect)
            screen.blit(scissors_image, cpu_scissors_image_rect)
            screen.blit(tiegame_image, tiegame_image_rect)
            tiegame_image_rect.x = 300
    if player_choice == "paper" :
        if cpu_choice == "paper":
            cpu_paper_image_rect.x = 500
            paper_image_rect.x = 100
            screen.blit(scissors_image, scissors_image_rect)
            screen.blit(scissors_image, cpu_scissors_image_rect)
            screen.blit(tiegame_image, tiegame_image_rect)
            tiegame_image_rect.x = 300
    if player_choice == "paper" :
        if cpu_choice == "scissors":
            cpu_rock_image_rect.x = 500
            paper_image_rect.x = 100
            screen.blit(paper_image, paper_image_rect)
            screen.blit(scissors_image, cpu_scissors_image_rect)
            screen.blit(youlose_image, youlose_image_rect)
            youlose_image_rect = 300
    if player_choice == "scissors" :
        if cpu_choice == "rock":
            cpu_rock_image_rect.x = 500
            scissors_image_rect.x = 100
            screen.blit(scissors_image, scissors_image_rect)
            screen.blit(scissors_image, cpu_scissors_image_rect)
            screen.blit(youlose_image, youlose_image_rect)
            youlose_image_rect.x = 300
    if player_choice == "rock" :
        if cpu_choice == "paper":
            cpu_paper_image_rect.x = 500
            rock_image_rect.x = 100
            screen.blit(rock_image, rock_image_rect)
            screen.blit(paper_image, cpu_paper_image_rect)
            screen.blit(youlose_image, youlose_image_rect)
            youlose_image_rect.x = 300

    pg.display.flip()

    pg.quit()