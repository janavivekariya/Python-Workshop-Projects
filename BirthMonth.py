month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

bd = str(input("Enter DOB in form of DD-MM-YYYY: "))

print(bd)
list = [bd]

a = month[int(bd[3:5])-1]

print("You were born in", a)
