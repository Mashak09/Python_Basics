per = input('nindo per endro monu/molu: ')
print('nindo ee gamel swagatha', per)

answer = input('neen ippa kandatho endl ulle, neen ippa right illeng left pgonu yodeg ponde: ').lower()

if answer == 'left':
    answer = input('wah mone, ippa neen pole do awude ulle neen swim akre illeng seedha ponde. neen swim akreng swim illeng walkg walk type aak: ')

    if answer == 'swim':
        print('nindo mosale thindth, che!!')
    elif answer == 'walk':
        print('neen walk walk bacchith marche!, che!!')
    else:
        print('nindotta bere endum option ille. Neen sothe!!')

elif answer == 'right':
    # You need to write something here
    print('neen right poyi! illa code missing ide!')  # placeholder

else:
    print('bere option illa, neen sothe!!')

print('Danyavadagalu', per)
