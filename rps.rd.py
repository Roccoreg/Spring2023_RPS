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
rock_image_rect.x = 0
paper_image_rect.x = 200
scissors_image_rect.x = 400
running = True

print("Let's play:")
print (choices0)
sleep (.5)
print ("Click on Rock, Paper, or Scissors")


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
                player_choice = "ROCK"
                cpu_choice = cpu_randchoice()
            # print(paper_image_rect.collidepoint(mouse_coords))
            # if collided then you clicked on the picture
            elif paper_image_rect.collidepoint(mouse_coords):
                print ("you clicked on paper")
                player_choice = "PAPER"
                cpu_choice = cpu_randchoice()
            # print(scissors_image_rect.collidepoint(mouse_coords))
            # if collided then you clicked on the picture
            elif scissors_image_rect.collidepoint(mouse_coords):
                print ("you clicked on scissors")
                player_choice = "SCISSORS"
                cpu_choice = cpu_randchoice
            else:
                print ("Try again, you did not click anything")
           
########## update ###################

############ draw ###################
screen.fill(BLACK)
# Rock is drawn on the screen
while running:
    if player_choice == "":
        screen.blit(rock_image, rock_image_rect)
        screen.blit(paper_image, paper_image_rect)
        screen.blit(scissors_image, scissors_image_rect)
    if player_choice == "ROCK" and cpu_choice == "SCISSORS":
        screen.blit (rock_image, rock_image_rect)
        screen.blit (scissors_image, scissors_image_rect)
    if player_choice == "ROCK" and cpu_choice == "PAPER":
        screen.blit (rock_image, rock_image_rect)
        screen.blit (paper_image, paper_image_rect)
    if player_choice == "ROCK" and cpu_choice == "ROCK":
        screen.blit (rock_image, rock_image_rect)
    if player_choice == "SCISSORS" and cpu_choice == "ROCK":
        screen.blit (scissors_image, scissors_image_rect)
        screen.blit (rock_image, rock_image_rect)
    if player_choice == "PAPER" and cpu_choice == "ROCK":
        screen.blit (paper_image, paper_image_rect)
        screen.blit (rock_image, rock_image_rect)
    if player_choice == "SCISSORS" and cpu_choice == "SCISSORS":
        screen.blit (scissors_image, scissors_image_rect)
        screen.blit (scissors_image, scissors_image_rect)
    if player_choice == "SCISSORS" and cpu_choice == "PAPER":
        screen.blit (scissors_image, scissors_image_rect)
        screen.blit (paper_image, paper_image_rect)
    if player_choice == "SCISSORS" and cpu_choice == "SCISSORS":
        screen.blit (scissors_image, scissors_image_rect)
    if player_choice == "PAPER" and cpu_choice == "PAPER":
        screen.blit (paper_image, paper_image_rect)

pg.quit()
     
    ########## update ###################

    ############ draw ###################
screen.fill(BLACK)



    

    # if cpu_choice == "rock":
    #     screen.blit(rock_image, rock_image_rect)


pg.display.flip()

pg.quit()