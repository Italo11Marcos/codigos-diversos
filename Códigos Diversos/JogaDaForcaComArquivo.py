import random

arq = open("arq.txt", "r")
linha = arq.read()
while linha:
    palavraSecreta = linha.split()
    for i in palavraSecreta:
        linha = arq.read()

#print(palavraSecreta)

palavra = random.choice(palavraSecreta)

palavraChave = []
palavraCorreta = []
totalChances = 20
tamanho = len(palavra)
acertos = 0;

for i in range(tamanho):
    palavraChave.append(palavra[i])
    palavraCorreta.append("-")

print("Animal com {} letras".format(tamanho))

for i in range(totalChances):
    print("{} Tentativas".format(totalChances - i))
    C = input()
    for j in range(tamanho):
        if C == palavraChave[j]:
            palavraCorreta[j] = C
            acertos+=1
            print(palavraCorreta)
    if acertos == tamanho:
        print("Acerto Miseravi")
        break

print(palavra)
            



    




    
