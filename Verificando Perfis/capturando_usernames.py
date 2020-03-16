#!Python3
#capturando_usernames.py - Esse script pega o username presente no link 

print('Iniciando...')

arq1 = open('links_users.txt', 'r')
arq2 = open('final_users.txt', 'w')

count = 0

linha = arq1.readline()
while linha:
    values = linha.split('/')
    save = values[-1]
    #print(save)
    arq2.write(save)
    linha = arq1.readline()
    count += 1

print(count)
print('Done...')

arq1.close()
arq2.close()
