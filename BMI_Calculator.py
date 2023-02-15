w =float(input("Enter weight in kg: "))
h =float(input("Enter weight in meters: "))

b = w/(h*h)

print("Your BMI is: ", b)

if b<=18.5:
    print("Underweight")

elif b>18.5 and b<=24.9:
    print("Normal Weight")

elif b>24.9 and b <=29.9:
    print("Overweight")

elif b>=30:
    print("Obesity")

