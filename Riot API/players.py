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

#Players com quem joguei
my_matches = watcher.match.matchlist_by_account(my_region, me['accountId'])
matchesIds = []
playersParticipants = []

for m in my_matches['matches']:
    matchesIds.append(m['gameId'])

for m in matchesIds:
    history_matches = watcher.match.by_id(my_region, m)
    for p in history_matches['participantIdentities']:
      playersParticipants.append(p['player']['summonerName'])

df = pd.DataFrame(playersParticipants)
print('criando o arquivo csv...')
df.to_csv('/home/charanjo/Desktop/players.csv', index=False, header=False)

