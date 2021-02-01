import random

palavraSecreta = ["baleia", "onça", "cachorro", "gato", "vaca", "boi", "urubu",
                "coelho", "rato", "elefante", "papagaio", "tatu", "formiga"]

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
            



    




    
