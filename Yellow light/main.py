#Constants
def main():
    #Constants
    DECEL           = 10                  
    GRAVACCEL       = 32.2
    PRECEPTION      = 1
    MPH_FEET        = 1.46667                                               #mph to feet conversion


    #Decoration stuff
    with open("./misc/picture","r") as f:                                   # kind of over the top but i wanted to review open() funciton haha
        picture = f.read()                                                  #assigns contents of picture file after reading it    
    print(picture)                                                          #shows picture


    #input
    print("INPUTS")
    Aproachgrade =   (float(input("What is the appraoch grade: " ))          )          
    Speedlimit   =   (float(input("What is the speed limit(MPH): "))*MPH_FEET)

    #processing
    Y = YLightFormula(DECEL, GRAVACCEL, Aproachgrade, PRECEPTION, Speedlimit)

    #output
    print(f"The Recommended Yellow light duration is {(Y):.2f}.")

def YLightFormula(d,g,G,T,V):
    return T+(V/((2*d)+(2*g*G)))                                            #formula for red light

main()