def addition(x,y):
    return x+y

def subtraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    return x/y

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

o = int(input("Choose the operation you want to perform: \n 1.Addition \n 2.Subtraction \n 3. Multiplication \n 4. Division \n"))

if o == 1:
   print(addition(x, y))
elif o == 2:
   print(subtraction(x,y))
elif o == 3:
    print(multiplication(x,y))
elif o == 4:
    print(division(x,y))


