print("Nando Simple-Caluclatorg nindo swagatha")

number1=input('First number id monu: ')
number2=input('Second Number id monu: ')
try:
    number1=float(number1)
    number2=float(number2)
except ValueError: # as told bewfore if the suer enters other than a number shows an error
    print('Number id monu neen endro ittónthu ulle')
    exit()

operation=input("Yed ayeng oru option choose aak (+, -, *, /): ")