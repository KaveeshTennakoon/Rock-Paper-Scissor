import random

def play():

    comp=random.choice(["r","p","s"])

    user=user_input()

    printing(comp)

    if user=="r" and comp=="r":
        print("Draw")
        return "d"
    elif user=="p" and comp=="p":
        print("Draw")
        return "d"
    elif user=="s" and comp=="s":
        print("Draw")
        return "d"
    elif user=="r" and comp=="s":
        print("You Wins")
        return "u"
    elif user=="p" and comp=="r":
        print("You Wins")
        return "u"
    elif user=="s" and comp=="p":
        print("You Wins")
        return "u"
    elif user=="s" and comp=="r":
        print("Computer Wins")
        return "c"
    elif user=="r" and comp=="p":
        print("Computer Wins")
        return "c"
    else:
        print("Computer Wins")
        return "c"

def user_input():
    flag=False
    while flag==False:
        user=input("Enter 'r' for rock, 'p' for paper, 's' for scissor: ")
        if user=="r":
            flag=True
        elif user=="p":
            flag=True
        elif user=="s":
            flag=True
    return user

def printing(x):
    if x=="r":
        print("Computer plays rock")
    elif x=="p":
        print("Computer plays paper")
    else:
        print("Computer plays scissor")

user_score=0
comp_score=0

rounds=int(input("Enter how many rounds does the game goes?: "))
print("**********************************************")
for i in range(rounds):
    print()
    res=play()
    if res=="u":
        user_score=user_score+1
    elif res=="c":
        comp_score=comp_score+1
print()
print("Your score: ",user_score)
print("Computer score: ",comp_score)
print()

if user_score > comp_score:
    print("Congratualtions! You Won The Game.")
elif user_score < comp_score:
    print("Computer Won. Better Luck Next Time.")
else:
    print("Game Draw")
