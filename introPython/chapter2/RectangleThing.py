#area of rectangles
#input
print("Enter the length and width of two rectangles.")
length1 = float(input("Length 1: "))
width1  = float(input("Width 1: " ))
length2 = float(input("Length 2: "))
width2  = float(input("Width2: "  ))
#processing
rect1 = length1 *width1                                     #rect1 area
rect2 = length2*width2                                      #rect2 area
#selection
if rect1 > rect2:                                           # if r1 is larger
    print("The first rectangles area is larger.")
elif rect2>rect1:                                           # if r2 is larger
    print("The second rectangles area is larger.")
else:                                                       # no need for elif and comparison bc the only other possiblity is equal
    print("the rectangles are equal in area.")  