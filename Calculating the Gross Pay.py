#Assigning Variables
hours_worked = float(input("Enter the hours worked: "))
rate_per_hour = float(input("Enter the rate per hour: "))

#Calculating the gross pay
gross_pay = hours_worked * rate_per_hour

#Printing the gross pay
print("The Gross pay is :  ",gross_pay)

#Printing to the file
f = open("C:\\Users\\LENOVO\\Desktop\\Python Files\\python.txt","a")
print("The Gross Pay is:  ", gross_pay , file=f)
f.close()
