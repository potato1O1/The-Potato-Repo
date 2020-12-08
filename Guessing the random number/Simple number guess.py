import random

userint = int(input("Guess the random number: "))
randn = random.randint(1, 5)

print(randn)

if userint == randn:
    print("correct")
else:
    print("wrong")
