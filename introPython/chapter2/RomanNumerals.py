#Roman Numerals
#input
num = int(input("Enter a number between 1 and 10: "))      #Prompt user for input to pass to selection
#selection
match num:                                                 #outputing number based off of input1   
    case 1 :
        print("I")
    case 2 :
        print("II")
    case 3 :
        print("III")
    case 4 :
        print("IV")
    case 5 :
        print("V")
    case 6 :
        print("VI")
    case 7 :
        print("VII")
    case 8 :
        print("VIII")
    case 9 :
        print("IX")
    case 10 :
        print("X")
    case _:
        print("You printed a number below or above 1-10.")  #output if they entered a invalid number
    