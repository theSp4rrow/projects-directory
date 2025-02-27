#Calories burnt on treadmill
CALORIESPM = 4.2                                                #calories burned per minute
print("___________CALORIES BURNED___________")   
               
for x in [10,15,20,25,30]:                                      #goes through each piece of data assiging it to x for processing later
                                          
    print(f"{x} Minutes calories burned: {int(x*CALORIESPM)}")  # prints burned calories multiplying the data by the 4.2 constant
