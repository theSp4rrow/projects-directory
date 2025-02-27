#planting grapevines   
# the book had the variables defined this way                                                                         
print("welecome to planting grape vines: ")    
print("---------------------------INPUT---------------------------")
R = float(input("Input the length of the row in feet: "))                                       #defining length
E = float(input("Input the amount of space by feet used in the post end assembely in feet: "))  #defining space
S = float(input("input the amount of space in between the vines in feet: "))                    #defining amoount of space between vines                                                                                  

V = ((R-(2*E))/S)                                                                               #formula
print("---------------------------OUTPUT---------------------------")
if (V % 1) == 0:                                                                                #if formula output is a int print it into a into
    print(f"Grape vines to plant in each row {int(V)}")                                                                               
else:                                                                                           
    print(f"Grape vines to plant in each row {"{:.2f}".format(V)}")                                                                   #else print as double but only print up to the hundreths place
input("Press any Key to quit: ")