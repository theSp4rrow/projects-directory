#Book club points
print("Welecome!")                                                                  
PurchasedBooks = int(input("How many books have you purchased this month: ")) #prompt user for amount of books purchased this month
Points         = 0                                                            #intialise point variable as in
if PurchasedBooks   == 0:                                                     #checking points and assigning them according to the key
    pass                                                                      #I passed because the points variable is already set to 0 so there is no reason to redifine it
elif PurchasedBooks ==2:                                                      
    Points = 5
elif PurchasedBooks ==4:
    Points = 15
elif PurchasedBooks ==6:
    Points = 30
elif PurchasedBooks ==8:
    Points = 60
print(f"The number of points you have earned is {Points} points.")            #Printing amount of points that were earned
