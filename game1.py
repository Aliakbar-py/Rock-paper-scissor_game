import random
print("lets play rock paper ")
game=["rock","paper","scissor"]
while True :
    user=input("select a option [rock ,paper ,scissor]:").lower()
    if user not in game:
        print("invalid choice")
    else :
        computer=random.choice(game).lower()
        print("computer choose:",computer)
    if user==computer:
        print("game is tie")
    elif user=="paper" and computer=="rock" :
        print("user win")
    elif user=="rock" and computer=="scissor" :
        print("user win")
    elif user=="scissor" and computer=="paper":
        print("user win")
    elif computer=="paper" and user=="rock":
        print("computer win")
    elif computer=="rock" and user=="scissor" :
        print("computer win")
    elif computer=="scissor" and user=="paper" :
        print("computer win")
else :
    print("terminate")