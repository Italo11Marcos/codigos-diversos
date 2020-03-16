#!Python3
#index.py
#Percorre o diretório indicado, altera o nome dos arquivos e copia o arquivos para outra pasta
import shutil, os

count = 0

#Percorre pastas, subpastas e arquivos no diretório
for folderName, subfolders, filenames in os.walk('/home/dti/Downloads/PosDoutoradoJuniorXML'):
    print('The current folder is ' + folderName)
    count += 1
    '''
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    '''
    
    #recebe o nome da pasta e cria uma nova variável com o novo nome
    name = folderName.split('/')
    nameatual = name[-1]
    #print(nameatual)
    newName = nameatual+'.xml'

    #newFolder = '/home/dti/Downloads/Curriculos_PosDoutoradoJunior_xml'

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)
        #Renomeia o arquivo
        #os.rename(folderName+'/'+filename, folderName+'/'+newName)
        #Copia o arquivo e cola em outra pasta
        #shutil.copy(folderName+'/'+filename, newFolder)

    

    print('')

print(count)