import random
def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value,max_value)

    return roll

while True:
    players=input('etthare aal benu nikk kaliko(2-4): ')
    if players.isdigit():
        players=int(players)
        if 2<= players <=4:
            break
        else:
            print('2-4 aal ikkonu monu')
    else:
        print('ad choice tappundu, wapad id')

max_score=50
players_scores=[0 for _ in range(players)]

while max(players_scores)<max_score:
    for player_idx in range(players):
        print('\n player number',player_idx +1,' turn has started ')
        print('nindo total score ', players_scores[player_idx,'\n'])
        current_score=0

    while True:
        should_roll=input('Nikk role aako manas unda (y)?: ')
        if should_roll.lower() !='y':
            break
        value = roll()
        if value==1:
            print('You rolled a 1! Turn done')
            current_score=0
            break
        else:
            current_score += value
            print('You rolled a:', value)
        print('Your score is:',current_score) 
    players_scores[player_idx]+=current_score
    print('Your total score is:',players_scores[player_idx])

max_score=max(player_scores)
winning_idx=players_scores.index(max_score)
print('player number', winning_idx+1,'is winner of the score of:',max_score)
