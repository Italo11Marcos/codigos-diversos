#!Python3
#usernames_to_instagram.py - Esse script pega o username e coloca num link do instagram 

print('Iniciando...')

arq1 = open('final_users.txt', 'r')
arq2 = open('instagram_profiles.txt', 'w')

count = 0

linha = arq1.readline()
while linha:
    values = linha
    instagram_link = 'https://www.instagram.com/'
    save = instagram_link + values
    arq2.write(save)
    linha = arq1.readline()
    count += 1

print(count)
print('Done...')

arq1.close()
arq2.close()
