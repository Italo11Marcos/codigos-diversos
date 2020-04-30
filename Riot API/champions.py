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


#Champions que mais apareceram nas minhas partidas
#minhas partidas
my_matches = watcher.match.matchlist_by_account(my_region, me['accountId'])

matchesIds = []
champs = []

#Id de cada partida
for m in my_matches['matches']:
    matchesIds.append(m['gameId'])

#O champions id de cada partida
for m in matchesIds:
    history_matches = watcher.match.by_id(my_region, m)
    for p in history_matches['participants']:
      champs.append(p['championId'])
#print(len(champs))

#Pega os dados da última versão do lol
latest = watcher.data_dragon.versions_for_region(my_region)['n']['champion']
# Informações dos champions
static_champ_list = watcher.data_dragon.champions(latest, False, 'pt_BR')
champ_dict = {}
for key in static_champ_list['data']:
    row = static_champ_list['data'][key]
    champ_dict[row['key']] = row['id']
#print(champ_dict)
names_champs = []
for c in champs:
  if str(c) in champ_dict:
    names_champs.append(champ_dict[str(c)])
#print(names_champs)    
df = pd.DataFrame(names_champs)
df.to_csv('C:\\Users\\charanko\\Documents\\champs.csv', index=False, header=False)