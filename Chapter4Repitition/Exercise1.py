#Bug collector
print("____________Bug Collector____________")
DAYS    = 5                                 #Constant because assignment specifys 5
bugs    = 0                                 #Used to keep track of bugs   

for x in range(0,DAYS):                     #should output 5 repititions
    print("Day",x+1)                        #prints day and the the repitition the loop is on
    bugs += int(input(" Bugs collected: "))  #collects and adds the amount of bugs found on specific day
print(f"\nTotal bugs collected {bugs}")