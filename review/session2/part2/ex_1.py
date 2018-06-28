weight = float(input("Enter your weight: "))
hight = float(input("Enter your hight: "))
h = (hight/100) 
print(weight, "kg")
print(h, "m")

BMI = (weight / (h*h))
print(BMI)

if(BMI < 16):
    print("Severely underweight")
elif(BMI < 18.5):
    print("Underweight ")
elif(BMI < 25):
    print("Normal")
elif(BMI < 30):
    print("Overweight")
else:
    print("Obese")
