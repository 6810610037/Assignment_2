#bmi
_type,mass,height = input().split()
mass = eval(mass)
height = eval(height)
if (_type == "m" or _type =="M"):
    BMI = mass / (height**2)
if (_type == "i" or _type =="I"):
    BMI = mass / (height**2) * 703
if(BMI > 0 and BMI <15):
    sequence = 1
elif(BMI >= 15 and BMI <16):
    sequence = 2
elif(BMI >= 16 and BMI <18.5):
    sequence = 3
elif(BMI >= 18.5 and BMI <25):
    sequence = 4
elif(BMI >= 25 and BMI <30):
    sequence = 5
elif(BMI >= 30 and BMI <35):
    sequence = 6
elif(BMI >= 35 and BMI <40):
    sequence = 7
elif(BMI > 40):
    sequence = 8
print(f"{BMI:.1f} {sequence}")