per=input('nindo per endro monu: ')
print('nindo ee gamel swagatha',per)

answer=input('neen ippa kandatho endl ulle, neen ippa right illeng left pgonu yodeg ponde: ').lower()
if answer == 'left':
    answer=input('wah mone, ippa neen pole do awude ulle neen swim akre illeng seedha ponde. neen swim akreng swim illeng walkg walk type aak')

    if answer=='swim':
        print('nindo mosale thindth,che!!')
    elif answer=='walk':
        print('neen walk walk bacchith marche!, che!!')
    else:
        print('nindotta bere endum option ille. Neen sothe!!')

elif answer=='right':
    print('oru bridge kittith, booldo pole undu neen front ponde back ponde')
    if answer=='back':
        print('neen back poye alle adk sothe')
    elif answer==('front'):
        print('nikk oru stranger kittra awuldotta mundre ille?')

        if answer=='yes':
            print('shabas mone! nikk awulu bangar thannal!, neen gendiye!')
        elif answer=='no':
            print('aa strrangerg bejar aith neen sothe')
        else:
            print('bere option ille, so neen sothe')

else:
    print('nindotta bere optioon undutt nirche, sorry you LOSE!!')

print('Thank you for plying this game: ', per)