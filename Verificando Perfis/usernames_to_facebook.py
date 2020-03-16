#!Python3
#usernames_to_instagram.py - Esse script pega o username e coloca num link do instagram 

print('Iniciando...')

arq1 = open('final_users.txt', 'r')
arq2 = open('facebook_profiles.txt', 'w')

count = 0

linha = arq1.readline()
while linha:
    values = linha
    facebook_profiles = 'https://www.facebook.com/'
    save = facebook_profiles + values
    arq2.write(save)
    linha = arq1.readline()
    count += 1

print(count)
print('Done...')

arq1.close()
arq2.close()
