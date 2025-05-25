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
    operators=random.choice(operators)
    #randomly selects an operator from the list of operators
    expr=str(left)+''+operators+''+str(right)
    #creates a string that looks like a mathematical expression ok like 10+20