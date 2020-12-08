#grading test example
answer = True
while answer:
    questions = [
        "What is the color of an orange?",
        "What is the color of banana?",
        "What is the color of an apple?",
        "What is the color of Grapes?",
        "What is the color of pineapple?"
    ]

    pnt = 0
    pnt1 = 0
    pnt2 = 0
    pnt3 = 0
    pnt4 = 0

    #question1
    print(questions[0])
    q1 = input("Answer: ")

    if q1 == "orange" or  q1 == "Orange" or q1 == "ORANGE":
        print("You are correct!")
        pnt += 10
    else:
        print("You are wrong!")
    print("\n")

    #question2
    print(questions[1])
    q2 = input("Answer: ")

    if q2 == "yellow" or  q2 == "Yellow" or q2 == "YELLOW":
        print("You are correct!")
        pnt1 += 10
    else:
        print("You are wrong!")
    print("\n")

    #question3
    print(questions[2])
    q3 = input("Answer: ")

    if q3 == "red" or  q3 == "Red" or q3 == "RED":
        print("You are correct!")
        pnt2 += 10
    else:
        print("You are wrong!")
    print("\n")

    #question4
    print(questions[3])
    q4 = input("Answer: ")

    if q4 == "violet" or  q4 == "Violet" or q4 == "VIOLET":
        print("You are correct!")
        pnt3 += 10
    else:
        print("You are wrong!")
    print("\n")

    #question5
    print(questions[4])
    q5 = input("Answer: ")

    if q5 == "yellow" or  q5 == "Yellow" or q5 == "YELLOW":
        print("You are correct!")
        pnt4 += 10
    else:
        print("You are wrong!")
    print("\n")

    total = pnt + pnt1 + pnt2 + pnt3 + pnt4
    rating = total / 5

    print("Your total score is", total)
    print("Your final rating is", rating)

    if rating > 7.0 and 7:
        print("You pass the damn test!")
    else:
        print("See you next semester!")
    
    tryagain = input("Do you want take the test again? type: YES/NO: ")
    if tryagain == "NO":
        answer = False
    else: 
        answer = True




