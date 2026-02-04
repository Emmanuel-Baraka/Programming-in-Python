#EMMANUEL BARAKA
#REG NO : BSCIT-05-0113/2024
"""A company decided to give a bonus to employee according to the following criteria :
Period of service                   Bonus
More than 10                          10%
>=6 and <=10                          8%
less than 6 years                     5%

Ask user for their salary and years of service and print the net bonus amount
"""
#Prompting the user to enter the salary
salary = float(input("Enter your salary: "))
years = int(input("Enter your period of service : "))

#if else statement
if (years > 10):
    bonus = salary * 0.1
   
elif ( years >= 6 and years <=10 ):
    bonus = salary * 0.08
    
else :
    bonus = salary * 0.06

print("The Net Bonus is: ",bonus)

#Printing to the file
f = open("C:\\Users\\LENOVO\\Desktop\\Python Files\\Python decision making.txt","w")
print("The NetBonus is : ", bonus , file=f)
f.close()
