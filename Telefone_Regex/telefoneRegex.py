#! python3
#telefoneRegex.py - Encontra correspôndencias para o padrão (xx)xxxxx-xxxx ou
#		    (xx)xxxx-xxxx no texto
# Ideias para melhorar o código: Verificar se o número encontrado existe

#Módulo regex - expressões regulares
import re

#Abre o arquivo e lê o conteúdo presente nele
ref_file = open('file.txt','r')

#A variável texto recebe todo o conteúdo do arquivo de entrada
texto = ref_file.read()

#O arquivo é fechado
ref_file = ref_file.close()

#print(texto)

#Regex para encontrar um número com a seguinte estrutura:
#(xx)xxxxx-xxxx || (xx)xxxx-xxxx
phoneRegex = re.compile(r'\(\d{2}\)\d{4}\-\d{4}|\(\d{2}\)\d{5}\-\d{4}')

#o método findall retorna todos os padrões encontrados
matches = phoneRegex.findall(texto)

print(matches)


