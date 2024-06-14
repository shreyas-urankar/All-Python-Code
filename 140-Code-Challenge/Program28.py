# Write a Python Program to calculate your Body Mass Index.

def bodymassindex(height_cm, weight):
    height_m=height_cm/100
    return weight / (height_m ** 2)
name=str(input("Enter your name:"))
height= float(input("Enter your height in centimeters:"))
weight=float(input("Enter your weigth in kg:"))
bmi=bodymassindex(height, weight)
print(f"{name}, your Body Mass Index (BMI) is: {bmi:.2f}")