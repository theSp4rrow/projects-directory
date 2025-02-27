print("-----------------------Land calculator-----------------------")                                                           
ACRE = 43560                                                                            #defining acre constant
total_squareft = int(input("Enter the totat number of square feet in the tract:"))      #getting the total acre input from the user
print(f"That is {total_squareft / ACRE:.2f} acres.")                                    #converting said input into acres and stopping the float
                                                                                        #making sure the float stops at two decimals
input("Press any key to exit: ")