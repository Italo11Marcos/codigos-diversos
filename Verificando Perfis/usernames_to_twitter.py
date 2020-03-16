#!Python3
#usernames_to_twitter.py - Esse script pega o username e coloca num link do twitter 

print('Iniciando...')

arq1 = open('final_users.txt', 'r')
arq2 = open('twitter_profiles.txt', 'w')

count = 0

linha = arq1.readline()
while linha:
    values = linha
    twitter_link = 'https://twitter.com/'
    save = twitter_link + values
    arq2.write(save)
    linha = arq1.readline()
    count += 1

print(count)
print('Done...')

arq1.close()
arq2.close()
