#!Python 3
#selectiveMove - Move todos os arquivos .txt
# de uma arvore para o diretório desejado
# Script utilisando o os.walk()
import os, shutil

def selectiveMove():

    folder = os.path.abspath("C:\\Users\\Charanko\\Desktop\\teste")
    dest = os.path.abspath("C:\\Users\\Charanko\\Desktop\\teste2")

    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith('.txt'):
                print(filename)
                shutil.move(os.path.join(foldername, filename), dest)
    print('Done.')


selectiveMove()

