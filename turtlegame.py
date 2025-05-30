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
    while True:
        racers=input('Input the number of racers (2-10):')
        if racers.isdigit(): #checks if the input is a number
            racers=int(racers) #converts the inpput to an  integer
        else:
            print('input number idonu monu:was tray aak ok')
            continue

        if  2<= racers <=10:
            return racers
        else:
            print('number 2-10 rangel ille monu. waapas enter aak')

def race(colors):#defines a function called race that takes a list of colors    
    turtle=create_turtles(colors) #calls the create_turtles function to create turtles with the given color
    while True: 
        for racer in turtle:
            distance=random.randint(1,20) #each turtle moves between 1 and 19 pixels together
            racer.forward(distance) #moves the current turtle forward by the distance calculated above

            x,y=racer.pos() #gets the x,y co-ordinate of the turtle and pos returns a tuple 
            if y>=height // 2-10

