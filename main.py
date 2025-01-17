import random
#Imports all the required functions form the game.py file
from game import add, sub, times, input_users_name

#Set the required varibles to the start numbers.
round = 1
score = 0
#Calls the function to request the player sets a name
player_name = input_users_name()

#While loop runs well round doesn't = 11 which results in the loop running 10 times for 10 questions
while round != 11:
    print("Question number", round)
    question = random.randint(1,3) #Randomly generates a number between 1 and 3 to pick the question type
    num1 = random.randint(0,10)
    num2 = random.randint(0,10)
    if question == 1: #If number generated was one runs the function for the add question
        score=add(score,player_name,num1,num2) 
    elif question == 2:
        score=sub(score,player_name,num1,num2)
    elif question == 3:
        score=times(score,player_name,num1,num2)
    round += 1 #Increments the round number by 1
print("Your final score is", score) #Prints final score after the 10th round

