# Write a python program using function to convert Celsius to Fahrenheit

def f_to_c(f):
    return 5*(f-32)/9

f=float(input("Enter temperature in f:"))
print(f"{f_to_c(f):.2f}°C" )
