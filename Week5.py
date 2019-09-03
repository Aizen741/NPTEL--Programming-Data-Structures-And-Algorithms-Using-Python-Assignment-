"""Week 5 Programming Assignment """

data = input()
result = {}

while data:
    (winner, loser, sets) = data.split(":")
    (winner_sets, loser_sets) = (0, 0)
    (winner_games, loser_games) = (0, 0)
    (winner_BO5, winner_BO3) = (0, 0)

    for set in sets.split(","):
        temp = set.split("-")

        temp[0] = int(temp[0])
        temp[1] = int(temp[1])

        if(temp[0] > temp[1]):
            winner_sets = winner_sets + 1
        else:
            loser_sets = loser_sets + 1

        winner_games = winner_games + temp[0]
        loser_games = loser_games + temp[1]

    if winner_sets >= 3:
        winner_BO5 = winner_BO5 + 1
    elif winner_sets < 3:
        winner_BO3 = winner_BO3 + 1


    for player in [winner,loser]:
        try:
            result[player]
        except:
            result[player] = [0,0,0,0,0,0]


        if player == winner:
            result[player][0] = result[player][0] + winner_BO5
            result[player][1] = result[player][1] + winner_BO3
            result[player][2] = result[player][2] + winner_sets
            result[player][3] = result[player][3] + winner_games
            result[player][4] = result[player][4] + loser_sets
            result[player][5] = result[player][5] + loser_games

        if player == loser:
            result[player][2] = result[player][2] + loser_sets
            result[player][3] = result[player][3] + loser_games
            result[player][4] = result[player][4] + winner_sets
            result[player][5] = result[player][5] + winner_games
    data = input()

result = sorted(result.items(), key=lambda t:t[1], reverse=True)
for element in result :
    print(element[0], element[1][0], element[1][1], element[1][2], element[1][3], element[1][4], element[1][5])














