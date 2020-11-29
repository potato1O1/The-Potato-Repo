print("Rock, Paper, Scissor Game"'\n'
"Type S for Scissor, P for Paper and R for Rock!")
print('\n')
p1 = input("[Player 1]Enter an attack: ")
p2 = input("[Player 2] Enter an attack: ")



if p1 == 'R' and p2 == 'S':
    print("Rock wins!")
elif p1 == 'S' and p2 == 'P':
    print("Scissor wins!")
elif p1 == 'P' and p2 == 'R':
    print("Paper wins!")
elif p1 == 'S' and p2 == 'R':
    print("Rock wins!")
elif p1 == 'P' and p2 == 'S':
    print("Scissor wins!")
elif p1 == 'R' and p2 == 'P':
    print("Paper wins!")
else:
    print("Invalid input")

    
