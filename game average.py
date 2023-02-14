score_1 = float(input("Enter Lebron's points for game 1: "))
score_2 = float(input("Enter Lebron's points for game 2: "))
score_3 = float(input("Enter Lebron's points for game 3: "))
score_4 = float(input("Enter Lebron's points for game 4: "))
score_5 = float(input("Enter Lebron's points for game 5: "))
score_6 = float(input("Enter Lebron's points for game 6: "))
score_7 = float(input("Enter Lebron's points for game 7: "))
score_8 = float(input("Enter Lebron's points for game 8: "))
score_9 = float(input("Enter Lebron's points for game 9: "))
score_10 = float(input("Enter Lebron's points for game 10: "))

combined_score = float(score_1 + score_2 + score_3 + score_4 + score_5 + score_6 + score_7 + score_8 + score_9 + score_10)

print('Lebron James combined for a total of', combined_score, 'points this season', end ='')

games_played = 10

print('A total of 10 games were played this season')

print('Press Enter to View Next Gen Stats')

input()

player_average = (combined_score / games_played)

print(f'Lebrons player average was {player_average:.2f} this season')


