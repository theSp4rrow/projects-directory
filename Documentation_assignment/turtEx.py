import turtle as t

def main():

    ScreenWidth         =  1800
    ScreenHeight        =  900
    half                =  2
    stepI               =  100
    stepD               = -100
    
    endLoX              =  ScreenWidth  // half
    endXneg             =  endLoX       -  ScreenWidth
    endLoY              =  ScreenHeight // half
    endYneg             =  endLoY       - ScreenHeight

    AnimationSpeed      = 0

    t.setup(ScreenWidth, ScreenHeight)
    t.speed(AnimationSpeed)
    t.hideturtle()
    #first quarter
    drawXYgraph(endLoX, endLoY, stepI, stepI)  # call from line 22 goto 34, when its done it comes back to line 22 
    #second quarter
    drawXYgraph(endXneg, endLoY, stepD, stepI)  # call from line 24 goto 34, when its done it comes back to line 24
    #Third quarter
    drawXYgraph(endLoX, endYneg, stepI, stepD)  # call from line 26 goto 34, when its done it comes back to line 26
    #fourth quarter
    drawXYgraph(endXneg, endYneg, stepD, stepD)  # call from line 28 goto 34, when its done it comes back to line 28

    t.done()  # finished

#                 endLoX, endLoY, stepI, stepI
#                900,     450,    100,   100
def drawXYgraph(endLoX , endLoY, stepX, stepY):

    startL = 0; x = 0; y = 0


    for count in range(startL, endLoX, stepX):                                  #starts at 0 ands at endLoX steps by 100  
        
        t.goto(x, y)                                                            # moves to these cordinates
        t.pendown()
        s = "x" + str(x) + ", " + "y" + str(y)                                  #converts x and y into strings and adds them to the s string for writing later
        t.write(s, align="left", font=("Arial", 7, "normal"))                   #aligns s after written left
        t.penup()           
        x = count                                                               

        print(count)  # tell what the value of count is!
    
        for count in range(startL, endLoY, stepY):                              #starts at 0 ands at endLoY steps by 100 nested loop used for y 

            #print(x, y)
            t.goto(x, y)                                                        # goes to x y
            t.pendown()         
            s = "x" + str(x) + ", " + "y" + str(y)                              #converts x and y into strings and adds them to the s string for writing later
            t.write(s, align="left", font=("Arial", 7, "normal"))               #aligns s after written left
            t.penup()    
            y = count

main()