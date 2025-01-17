import random
from game import add, sub, times, input_users_name

round = 1
score = 0

player_name = input_users_name()

while round != 11:
    print("Question number", round)
    question = random.randint(1,1)
    num1 = random.randint(0,10)
    num2 = random.randint(0,10)
    if question == 1:
        score=add(score,player_name,num1,num2)
    elif question == 2:
        score=sub(score,player_name,num1,num2)
    elif question == 3:
        score=times(score,player_name,num1,num2)
    round += 1
print("Your final score is", score)

