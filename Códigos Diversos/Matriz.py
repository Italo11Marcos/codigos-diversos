n_linhas = 3
n_colunas = 3
valor = 0
	
matriz = []
for i in range(n_linhas):	    
    linha = [] 
    for j in range(n_colunas):
        x = int(input())
        linha += [x]
    matriz += [linha]


print(matriz)
