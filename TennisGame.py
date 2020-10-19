import numpy as np
import pandas as pd
####Score
#ID	Game	Player	Score
# 1	1	A	11
# 2	1	B	7
# 3	2	A	15
# 4	2	C	13
# 5	3	B	11
# 6	3	D	9
# 7	4	D	11
# 8	4	A	5
# 9	5	A	11
# 10	6	B	11
# 11	6	C	2
# 12	6	D	5
#
# Game
# ID	Winner	Date
# 1	A	2017-01-02
# 2	A	2016-05-06
# 3	B	2017-12-15
# 4	D	2016-05-06
#
# Player
# ID	Name	LastName
# A	Phil	Watertank
# B	Eva	    Smith
# C	John	Wick
# D	Bill	Bull
# E	Lisa	Owen
import pandas as pd
import numpy as np
player = pd.DataFrame([['A','Phil','Watertank'],['B','Eva','Smith'],['C','John','Wick'],['D','Bill','Bull'],['E','Lisa','Owen']],
                      columns=['id', 'name', 'lastname'])
score = pd.DataFrame([[1,1,'A',11],[2,1,'B',7],[3,2,'A',15],[4,2,'C',13],[5,3,'B',11],[6,3,'D',9],[7,4,'D',11],[8,4,'A',5],[9,5,'A',11],[10,6,'B',11],[11,6,'C',2],[12,6,'D',5]],
                     columns=['score_id', 'game', 'player', 'score'])
game = pd.DataFrame([[1,'A','2017-01-02'],[2,'B','2016-05-06'],[3,'C','2017-12-15'],[4,'D','2017-12-15']],
                    columns=['id', 'winner', 'date'])
#print(game)
#print(player['id'])
#print(player[player['id']=='A'])
#print(player.loc[player['id']=='A'])
#print(player.query('id == "A"'))
###############################
#print(player[['id','name']])
#############################
#print(player.loc[player['id']=='A'][['id','name']])
#print(player[['id','name']].loc[player['id']=='A'])
#print(player.query('id=="A"')[['id','name']])
#print(player[['id','name']].query('id=="A"'))
#######################################
#print(player.loc[player['name']=='Lisa',['lastname']].iat[0,0])
########################################
#print(pd.merge(player, score, how='left', left_on=player['id'], right_on=score['player']))
#######################
##############1)Show the average score of each player, even if they didn't play any games.
################Expected output (Player ID, Name, Average Score)
#print(pd.merge(player, score, how='left', left_on=player['id'], right_on=score['player']).groupby('player')['score'].mean())####mean va group by ghabele jabejayi nistand###
####################
# #####2)The score table is corrupted: a game can only have two players (not more, not less). Write a query that identifies and only shows the valid games and their winner.
# Expected output (Game,Winner)
#print(pd.merge(score, game, how='inner', left_on=score['game'], right_on=game['id'])[['game', 'winner']].drop_duplicates())
#
# Bonus: as an additional challenge, you can also display the winner's score. The condition described above should still apply.
# Expected output (Game, Winner, Winner Score)
#####print(pd.merge(score, game, how='inner', left_on=score['game'], right_on=game['id'])[['game', 'winner']].drop_duplicates())
#print(pd.merge(score, game, how='inner', left_on=score['game'], right_on=game['id']).groupby(['game','winner'])['score'].max())
#######################
####Show the score of players for games that they lost. Expected output (Game ID, Player Name, Player LastName, Score)
# SELECT a.GameId, p.Name AS "PlayerName", p.LastName AS  "PlayerLastname" , a.Score
# FROM Player  p
# JOIN (SELECT s.Player, g.GameId , MIN(S.Score) AS "Score"
# FROM Score s
# JOIN GAME g
# ON s.Game=g.GameID
# GROUP BY Game) a
# ON a.Player=p.PlayerId;
################################
from functools import reduce
#dfs=[score,game,player]
#df_final=reduce(lambda score,game:pd.merge(score,game,left_on=score['game'], right_on=game['id']), dfs)
#print(df_final)
#pd.merge(pd.merge(player, game,how="inner", left_on='id', right_on='player',score,how="inner",left_on='game',right_on='id'))
#game_score=pd.merge(score,game,how="inner",left_on='game',right_on='id').groupby('game')['score'].min()
####################################
# print(score.groupby('game')['score'].min())
# print(score.groupby('game').min()['score'])
# print(score.groupby(['game']).min()['score'])
###########################
print((score.groupby(['game']).min())

#print(game_score)
#game_score=pd.merge(score,game,how="inner",left_on=score['game'],right_on=game['id']).groupby('game')[['game','score','player']].min()
#print(pd.merge(game_score,player,how="inner",left_on=game_score['player'],right_on=player['id'])[['game','name','lastname','score']])