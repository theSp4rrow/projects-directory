#compound interest calculator
print("welecome to comopound interest calculator!")     
print("\n\n--------------------INPUT---------------------")
P = float(input("enter the princple: "))                                     #define principle
r = float(input("enter the intrest rate: "))/100                             #define usury
n = float(input("enter times the intrest is compounded: "))                  #number of times intrest is compounded
t = float(input("what is the specified number of years: "))                  #how many years

A = P*(1+(r/n))**(n*t)                                                       #compound intrest formula
print("\n\n--------------------OUTPUT--------------------\n")
print(f"The output is {"{:.2f}".format(A)}.")                                #output up to the hundreds place
print("\n----------------------------------------------\n")

print((input("Press any key to quit: ")))
