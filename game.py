
import random
def input_users_name():
    player_name = input("Hello, what is your name?")
    return player_name

def user_answer(player_name,symbol,num1,num2):
    repeat = True
    while repeat:
        print("Please answer the question", num1, symbol, num2, "=")
        try:
            useranswer = int(input("Hello " + player_name + " What is your answer?"))
            return useranswer 
        except ValueError:
            print("Please enter a whole number!\n")
            repeat=True

def correct(score):
        score += 1
        print("You got the answer right!\nYour score is now", score)
        return score

def incorrect(score):
        print("You got the answer wrong!\nYour score is still", score)    
        return score

def add(score,player_name,num1,num2):
    symbol="+"
    useranswer=user_answer(player_name,symbol,num1,num2)
    if num1+num2==useranswer:
        score=correct(score)
        return score
    else:
        score=incorrect(score)
        return score

def sub(score,player_name,num1,num2):
    symbol="-"
    useranswer=user_answer(player_name,symbol,num1,num2)
    if num1-num2==useranswer:
        score=correct(score)
        return score
    else:
        score=incorrect(score)
        return score
       
def times(score,player_name,num1,num2):
    symbol="*"
    useranswer=user_answer(player_name,symbol,num1,num2)
    if num1*num2==useranswer:
        score=correct(score)
        return score
    else:
        score=incorrect(score)
        return score