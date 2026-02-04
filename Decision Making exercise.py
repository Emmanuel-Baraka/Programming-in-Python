#EMMANUEL BARAKA
#REG NO : BSCIT-05-0113/2024

subject1 = int(input("Enter the marks for subject 1: "))
subject2 = int(input("Enter the marks for subject 2: "))
subject3 = int(input("Enter the marks for subject 3: "))

#calculating the average score
avgscore = (subject1 + subject2 + subject3)/3
print(avgscore)

#if statement

if (avgscore >=70 and avgscore <=100):
    grade = "A"
    print("Average grade is A")
    
elif(avgscore >=60 and avgscore <=69):
    grade = "B"
    print("Average grade is B")

elif(avgscore >=50 and avgscore <=59):
    grade = "C"
    print("Average grade is C")

elif(avgscore >=40 and avgscore <=49):
    grade = "D"
    print("Average grade is D")

elif(avgscore >=0 and avgscore <=39):
    grade = "Fail"
    print("Average grade is Fail")

else:
    print("Invalid input")

#Printing to the file
f = open("C:\\Users\\LENOVO\\Desktop\\Python Files\\Python decision making.txt","a")
print("Average grade is : ", grade , file=f)
f.close()
