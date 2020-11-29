operator = input("\n+"
"\n-"
"\n*"
"\n/"
"\nChoose an operator: ")

number = ""
number2 = ""

while True:
    try:
        number = float(input("Enter first number: "))
    except ValueError:
        print("Invalid number!")
        continue
    try:
        number2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number!")  
        continue      
    else:
        break

if operator == "+":
    print("{:.2f}".format(number + number2))
elif operator == "-":
    print("{:.2f}".format(number2 - number2))
elif operator == "*":
    print("{:.2f}".format(number * number2))
elif operator == "/":
    print("{:.2f}".format(number / number2))
else: 
    print("Invalid operator!") 
