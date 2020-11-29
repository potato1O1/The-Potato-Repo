#example questions 
questions = [
    "Question one..blah blah blah",
    "Question two..blah blah blah",
    "Question three..blah blah blah"
]

anss = 0
ans2s = 0
ans3s = 0

#Question number 1
print(questions[0])
ans = input("Answer: ")
if ans == 'a':
    print("Correct Answer!")
    anss += 10
    print('You got',anss, 'points')
else:
    print("Wrong answer!")
    
print("\n")

#Question number 2
print(questions[1])
ans2 = input("Anwser: ")
if ans2 == 'b':
    print("Correct Answer!")
    ans2s += 10
    print('You got',ans2s, 'points')
else:
    print("Wrong answer!")

print("\n")

#Question number 3
print(questions[2])
ans3 = input("Answer: ")
if ans3 == 'c':
    print("Correct Answer!")
    ans3s += 10
    print('You got',ans3s, 'points')
else:
    print("Wrong answer!")


print('Total points gained:',anss + ans2s + ans3s)
