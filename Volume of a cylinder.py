import math
#Reading the radius
radius = 2
volume = 4/3 * math.pi * radius * radius
print("The volume is :  ", volume)

#Printing to the file
f = open("C:\\Users\\LENOVO\\Desktop\\Python Files\\python.txt","a")
print("The volume is: ", volume , file=f)
f.close()
