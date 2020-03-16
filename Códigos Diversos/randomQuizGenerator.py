#! python3
#randoQuizGenerator.py - Cria provas com perguntas e respostas em
#ordem aleatória, juntamente com os gabaritos contendo as respostas

import random

#os dados para as provas. As chaves são os estados e os valores são as capitais
capitals = {'Minas Gerais':'Belo Horizonte', 'Sao Paulo':'Sao Paulo',
            'Rio de Janeiro':'Rio de Janeiro', 'Espirito Santo':'Vitoria',
            'Goias':'Goiania', 'Parana':'Curitiba',
            'Santa Catarina':'Florianopolis',
            'Rio Grande do Sul':'Porto Alegre',
            'Bahia':'Salvador', 'Maranhao':'Sao Luis', 'Alagoas':'Maceio',
            'Paraiba':'Joao Pessoa', 'Para':'Belem', 'Ceara':'Fortaleza',
            'Roraima':'Boa Vista', 'Amazonas':'Manaus', 'Sergipe':'Aracaju',
            'Acre':'Rio Branco', 'Amapa':'Macapa', 'Piaui':'Teresina',
            'Mato Grosso':'Cuiaba', 'Mato Grosso do Sul':'Campo Grande',
            'Para':'Belem', 'Roraima':'Boa Vista', 'Rondonia':'Porto Velho',
            'Rio Grande do Norte':'Natal', 'Tocantins':'Palmas',
            'Pernambuco':'Recife', 'Distrito Federal':'Brasilia'}

#Gera 27 arquivos contendo as provas
for quizNum in range(27):
    #Cria os arquivos com as provas e os gabaritos das respostas
    quizFile = open('capitalsquiz%s.txt' % (quizNum+1), 'w')
    answerKeyFile = open('capitalsquiz_answer%s.txt' % (quizNum+1), 'w')

    #Escreve o cabeçalho da prova
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((''*20)+'State Capitals Quiz(Form %s)'%(quizNum+1))
    quizFile.write('\n\n')

    #Embaralha a ordem dos estados
    states = list(capitals.keys())
    random.shuffle(states)

    #Percorre todos os 27 estados em um loop, criando uma pergunta para cada um
    for questionNum in range(27):
        #Obtem respostas corretas e incorretas
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers,3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        #Grava a pergunta e as opções de resposta no arquivo de prova
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1,
                                                             states[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')
        

        #Grava o gabarito com as respostas em um arquivo.
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[
            answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
    

