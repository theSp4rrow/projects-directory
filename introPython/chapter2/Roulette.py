#Routlette wheels colands
output = ''

print("    __________________________")
print("   /                          \\")
print("  /       ROULETTTE WHEEL      \\")
num  = int(input(" /   Enter a between 0 and 36:  \\"))
print("/                                \\")
print("\\                                /")
if num ==0:
    output = ("green")
elif num>=1 and num<=10:
    if num%2 ==0:
        output =("black")
    else:
        output =("red")
elif num>=11 and num<=18:
    if num%2 ==0:
        output =("red")
    else:
        output("black")
elif num>=19 and num<=28:
    if num%2 ==0:
        output("black")
    else:
        output("red")
elif num>=29 and num<=36:
    if num%2 ==0:
        output("red")
    else:
        output("black")
else:
    print("You entered a number out of the range of 0 and 36")
print(f" \\             {output}")
print("  \\____________________________/")
