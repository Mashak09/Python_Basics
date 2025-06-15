print("Nando Simple-Caluclatorg nindo swagatha")

number1=input('First number id monu: ')
number2=input('Second Number id monu: ')
try:
    number1=float(number1)
    number2=float(number2)
except ValueError: # as told before if the user enters other than a number shows an error
    print('Number id monu neen endro ittónthu ulle')
    exit()

operation = input("Yed ayeng oru option choose aak (+, -, *, /): ")

if operation == '+':
    result = number1 + number2
elif operation == '-':
    result = number1 - number2
elif operation == '*':
    result = number1 * number2
elif operation == '/':
    if number2 != 0:
        result = number1 / number2
    else:
        print('divide by 0 awulle monu')
        exit()
else:
    print('nen endro operation itro la')
    exit

print(f"result is:{result}") #gives  the result in a formatted way
# now we ask the user if he wants to calculöate again
choice=input('Do you want to calculate again?(Yes/No): ').lower()
if choice != 'yes':
    print('okay bro! Bye Bye')
    exit()


