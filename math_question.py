import random
import time
# random library is used to generate random numbers 
# time library is used to measure the time taken by the user to answer the question
operators =['+','-','*']
# defnies the operators that can be used in the questions
Min_Num=10
Max_Num=100
Total_Problems=10
# defines the minimum and maximum numbers that can be used in the questions 
def generate_problem():
    left=random.randint(Min_Num,Max_Num)
    right=random.randint(Min_Num,Max_Num)
    # generates two random numbers between the minimum and maximum numbers
    operator=random.choice(operators)
    #randomly selects an operator from the list of operators
    expr=str(left)+operator+str(right)
    #creates a string that looks like a mathematical expression ok like 10+20
    answer=eval(expr)
    return expr, answer
    #genrates the expression and the answer to the expression
    
wrong=0
#no of wrong answers given by the user
input('quiz start madana macha!')
print('-----------------------')
#prints the line to indicate the start of the quiz
start_time=time.time()
#