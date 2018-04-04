#Cal300KP ver0.00.02 - 04.04.2018
#Main file for Cal300KP
#TO-DO:-> loop back to choice after calculation,
#Changelog: 0.00.01 -> 0.00.02:
#-Saving results to txt file.

from defcal import *


logo = 0
while logo < 3:
    print('###Cal300KP###')
    logo += 1
print("Select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Pithaghoras Statment")
choice = input("Enter choice(1/2/3/4/5):")

num1 = float(input("Enter first number:"))
num2 = float(input("Enter secend number:"))

if choice == "1":
    print(add(num1, num2))
    f = open('resultstxt.txt', 'w')
    f.write((str(add(num1, num2))))
    f.close()
elif choice == "2":
    print(sub(num1, num2))
    f = open('resultstxt.txt', 'w')
    f.write((str(min(num1, num2))))
    f.close()
elif choice == "3":
    print(multi(num1, num2))
    f = open('resultstxt.txt', 'w')
    f.write((str(multi(num1, num2))))
    f.close()
elif choice == "4":
    print(div(num1, num2))
    f = open('resultstxt.txt', 'w')
    f.write((str(div(num1, num2))))
    f.close()
elif choice == "5":
    print(pit(num1, num2))
    f = open('resultstxt.txt', 'w')
    f.write((str(pit(num1, num2))))
else:
   print("Invalid input")
print("###CAL300KP###")
