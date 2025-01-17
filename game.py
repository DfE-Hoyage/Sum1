
import random
def input_users_name():
    player_name = input("Hello, what is your name?")
    return player_name

def user_answer(player_name,symbol,num1,num2):
    repeat = True 
    while repeat: #Repeats the below until the user inputs a whole number
        print("Please answer the question", num1, symbol, num2, "=")
        try: #User validation check for whole number
            useranswer = int(input("Hello " + player_name + " What is your answer?"))
            return useranswer 
        except ValueError:
            print("Please enter a whole number!\n")
            repeat=True

#Function for incrementing the score and printing it out when the user gets a question correct
def correct(score):
        score += 1
        print("You got the answer right!\nYour score is now", score)
        return score

#Function for printing out the score when the user gets a question wrong
def incorrect(score):
        print("You got the answer wrong!\nYour score is still", score)    
        return score

# Add question function
def add(score,player_name,num1,num2):
    symbol="+"
    useranswer=user_answer(player_name,symbol,num1,num2) #Calls the function to request user answer to the question.
    if num1+num2==useranswer: #Checks users answer is correct and calls the correct or incorrect answer function.
        score=correct(score)
        return score
    else:
        score=incorrect(score)
        return score
    
#Subtraction question function
def sub(score,player_name,num1,num2):
    symbol="-"
    useranswer=user_answer(player_name,symbol,num1,num2)
    if num1-num2==useranswer:
        score=correct(score)
        return score
    else:
        score=incorrect(score)
        return score
    
#Multiplication question function       
def times(score,player_name,num1,num2):
    symbol="*"
    useranswer=user_answer(player_name,symbol,num1,num2)
    if num1*num2==useranswer:
        score=correct(score)
        return score
    else:
        score=incorrect(score)
        return score