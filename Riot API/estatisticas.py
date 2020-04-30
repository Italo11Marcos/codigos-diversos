#Recuperar todos os players com quem joguei

#Importando as libraries que usaremos
from riotwatcher import LolWatcher, ApiError
import pandas as pd

#Variáveis globais
api_key = 'RGAPI-8750ec45-5e3f-4d68-ba18-9427adfb9b00' #A api_key só funciona por 24h, vai ter que ficar trocando
watcher = LolWatcher(api_key)
nickname = 'HulkiAzul'
my_region = 'br1'

#Recuperar id, accountid, name e level da conta
me = watcher.summoner.by_name(my_region, nickname)
my_id = me['id']
my_accountId = me['accountId']
my_name = me['name']
my_summonerLevel = me['summonerLevel']
#print('Id: ', my_id, '\n', 'AccountId: ', my_accountId, '\n', 'Name: ', my_name, '\n', 'SummonerLevel: ', my_summonerLevel)

#Recuperar quantidade de partidas nessa season
my_matches = watcher.match.matchlist_by_account(my_region, my_accountId)
quantidade_partidas = my_matches['totalGames']
#print('Quantidade de partidas jogadas: ',quantidade_partidas)

#Pega algumas estatisticas das partidas
my_matches = watcher.match.matchlist_by_account(my_region, me['accountId'])
matchesIds = []
for m in my_matches['matches']:
    matchesIds.append(m['gameId'])

estatisticas = []
for m in matchesIds:
    history_matches = watcher.match.by_id(my_region, m)
    teams = {}
    teams['Win Blue'] = history_matches['teams'][0]['win']
    teams['First Tower Blue'] = history_matches['teams'][0]['firstTower']
    teams['Tower Kills Blue'] = history_matches['teams'][0]['towerKills']
    teams['Heralds Kills Blue'] = history_matches['teams'][0]['riftHeraldKills']
    teams['First Blood Blue'] = history_matches['teams'][0]['firstBlood']
    teams['First Inhibitor Blue'] = history_matches['teams'][0]['firstInhibitor']
    teams['Inhibitor Kills Blue'] = history_matches['teams'][0]['inhibitorKills']
    teams['First Baron Blue'] = history_matches['teams'][0]['firstBaron']
    teams['Baron Kills Blue'] = history_matches['teams'][0]['baronKills']
    teams['First Dragon Blue'] = history_matches['teams'][0]['firstDragon']
    teams['Dragon Kills Blue'] = history_matches['teams'][0]['dragonKills']
    teams['First Herald Blue'] = history_matches['teams'][0]['firstRiftHerald']
    teams['Win Red'] = history_matches['teams'][1]['win']
    teams['First Tower Red'] = history_matches['teams'][1]['firstTower']
    teams['Tower Kills Red'] = history_matches['teams'][1]['towerKills']
    teams['Heralds Kills Red'] = history_matches['teams'][1]['riftHeraldKills']
    teams['First Blood Red'] = history_matches['teams'][1]['firstBlood']
    teams['First Inhibitor Red'] = history_matches['teams'][1]['firstInhibitor']
    teams['Inhibitor Kills Red'] = history_matches['teams'][1]['inhibitorKills']
    teams['First Baron Red'] = history_matches['teams'][1]['firstBaron']
    teams['Baron Kills Red'] = history_matches['teams'][1]['baronKills']
    teams['First Dragon Red'] = history_matches['teams'][1]['firstDragon']
    teams['Dragon Kills Red'] = history_matches['teams'][1]['dragonKills']
    teams['First Herald Red'] = history_matches['teams'][1]['firstRiftHerald']
    estatisticas.append(teams)
df = pd.DataFrame(estatisticas)
df.to_csv('C:\\Users\\charanko\\Documents\\estatisticas_lol.csv', index=False)

