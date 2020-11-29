name = input("Enter you name: ")
print("Hello!", name, "Please answer the following questions:")
question1 = '''What color is blue?
a. yellow
b. blue
c. black
Enter Answer: '''
q1 = input()

q2 = input('''What color is an orange?
a. orange
b. violet
c. green
Enter Answer: ''')

q3 = input('''What color is an apple?
a. black
b. red
c. pink
Enter Answer: ''')

q4 = input('''Is this python code?
a. No
b. Maybe
c. Yes
Enter Answer: ''')

q5 = input('''Are you an idiot?
a. Absolutely, YES!
b. Hell yuhh!
c. No.
Enter Answer: ''')

print("")
print(name)
print("Result:")

p = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
if q1 == "b":
    p += 10
    print("Question 1. Correct!", "+", p, "points!")
else:
    print("Question 1. Wrong")
    p = 0

if q2 == "a":
    p2 += 10
    print("Question 2. Correct!", "+", p2, "points!")
else:
    print("Question 2. Wrong")
    p2 = 0

if q3 == "b":
    p3 += 10
    print("Question 2. Correct!", "+", p3, "points!")
else:
    print("Question 2. Wrong")
    p3 = 0 

if q4 == "c":
    p4 += 10
    print("Question 2. Correct!", "+", p4, "points!")
else:
    print("Question 2. Wrong")
    p4 = 0 

if q5 == "c":
    p5 += 10
    print("Question 2. Correct!", "+", p5, "points!")
else:
    print("Question 2. Wrong")
    p5 = 0 

print("Overall points:", p + p2 + p3 + p4 + p5)
