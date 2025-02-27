import turtle as t
#CONSTANTS 
WIDTH           =    500                    #Width 
HEIGHT          =    500                    #Height
CONVERTNEG      =   -1                      #used to convert ints or floats into negatives
HALF            =    2                      # used to divide no magic numbers
FONTSIZE        =    20                      # font size for the WriteIntials Function
INTIALS         =    "AAA"                  # intials   for the WriteIntials Function
SPEED           =    10
INTIALSCOUNT    =    3
#turtle settings
t.screensize(WIDTH,HEIGHT)                  #sets screensize equal to width and height
t.hideturtle()                              #hides turtle
t.speed(SPEED)                              #determines animation speed

def main():
    
    drawGrid()                             #calls draw grid
    t.goto(WIDTH/2+30,HEIGHT/2+25)         #moves turtle in a way so that write intials is above Draw AAA
    WriteIntials(INTIALS)                  # calls write intials
    DrawAAA(WIDTH/HALF,HEIGHT/HALF)        #passes half width and half height to draw

def DrawAAA(x,y):
    t.penup()
    t.pensize(2.5)
    t.goto(x,y)
    t.penup()
    offset = x                             # Used to move the letter a after each iteration so it doesnt draw over itself
    for x in range(INTIALSCOUNT):          #Iterates over drawing the letter A for intial count times
        t.pendown()
        t.left(70)
        t.forward(20)
        t.right(140)
        t.forward(20)
        t.penup()
        t.backward(10)
        t.right(110)
        t.pendown()
        t.forward(7.5)
        t.penup()
        offset+=20
        t.goto(offset,y)   
        t.right(180)
        t.hideturtle()    

        

def WriteIntials(intials):                  #Simply writes intials aligning them in the center of where the turtle is located
    t.write(intials, font=("Arial", FONTSIZE, "normal"),align="center")

def drawGrid ():                            # Draws grid for making sure that the intials are in the correct area
    #Draw x axis
    t.penup()
    t.goto(WIDTH*CONVERTNEG,0)
    t.pendown()
    t.forward(WIDTH*2)
    #Draw Y axis
    t.penup()
    t.goto(0,HEIGHT*CONVERTNEG)
    t.pendown()
    t.left(90)
    t.forward(HEIGHT*2)
    t.penup()
    t.right(90)

main()                                      # calls  main
t.done()                