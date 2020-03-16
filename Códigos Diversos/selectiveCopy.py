#!Python3
# selectiveCopy: Copia todos os arquivos ".txt" para o diretório desejado
import os, shutil

source = os.path.abspath("C:\\Users\\Charanko\\Desktop\\teste")
destiny = os.path.abspath("C:\\Users\\Charanko\\Desktop\\teste1")

search = os.listdir(source)
for files in search:
    if files.endswith(".txt"): #Pode mudar a extensão
        shutil.copy(os.path.join(source, files), destiny)
