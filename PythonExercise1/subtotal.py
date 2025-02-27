subtotal = 0.0      
SALESTAX = .07                                                              #sets default total value
print("---------------INPUT---------------\n")
for x in range(1,6):                                                        #prompt user for the price of the individual item 5 times
    cost = float(input(f"enter cost of item {x}: "))                        # input
    subtotal +=cost                                                         #adds cost to subtotal
subtotal =float("{:.2f}".format(subtotal))                                  # makes it so float it limited to the hundreds place 
print("\n---------------OUTPUT---------------\n")
print("Your subtotal came out to be " +str(subtotal))                       #prints a string appended to the float converted to a string
print(f"Sales tax is {"{:.2f}".format(subtotal*SALESTAX)}")                 #prints the sales tax up to the hundreds place
print(f"Your total is {"{:.2f}".format(subtotal+(subtotal*SALESTAX))}\n")   #prints the total with the sales tax and the subtotal added
input("Press any key to quit: ")