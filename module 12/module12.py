import random

while True:
    my_answer = input("choose: rock,paper or scissor: ")
    my_answer = my_answer.lower()
    if my_answer=="quit":
        break
    
    if my_answer!= "rock" and my_answer!="paper" and my_answer!="scissor":
        print("please choose correct answer")
        continue
    
    computer_answer = random.choice(["rock","paper","scissor"])
    print(f"computer chose: {computer_answer}")
    
    if my_answer==computer_answer:
        print("draw")
        continue
    elif my_answer=="paper" and computer_answer=="rock" or  my_answer=="rock" and computer_answer=="scissor" or  my_answer=="scissor" and computer_answer=="paper":
        print("you win")
        break
    else:
        print("you lose! try again")