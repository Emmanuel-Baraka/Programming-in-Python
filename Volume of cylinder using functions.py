import math
#EMMANUEL BARAKA
#REG NO : BSCIT-05-0113/2024
#Volume of cylinder
def cylinderVolume(radius,height):

    if radius < 0 or height <0 :
        print("Dimensions cannot be negative")

    volume = math.pi *(radius ** 2)* height
    return round(volume, 2)
   

r = float(input("Enter the radius of the cylinder: "))
h = float(input("Enter the height of the cylinder: "))



print(f"The volume of the cylinder is: {cylinderVolume(r,h)}")
