import turtle
#for drawing and animations
import time
#used here to pause the screen before the program ends
import random 
#used to generate random numbers for the turtle game
WIDTH, HEIGHT=400,500
#defines the width and height of the turtle screen
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']
def get_number_of_racers(): #defines a function to get the number of racers
    racers=0
    While True:
        racers=input('Input the number of racers (2-10):')