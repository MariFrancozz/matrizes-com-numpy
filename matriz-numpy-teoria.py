import numpy as dsa

# Array criado a partir de uma lista Python
arr1 = dsa.array([10, 21, 32, 43, 48, 15, 76, 57, 89])
print(arr1)

# Um objeto do tipo ndarray é um recipiente multidimensional de itens do mesmo tipo e tamanho
type(arr1)

# Verificando o formato do array
arr1.shape
print(arr1)

# Imprimindo um elemento específico no array
arr1[4] 

# Indexação
arr1[1:4] 

# Indexação
arr1[1:4+1] 

# Cria uma lista de índices
indices = [1, 2, 5, 6]

# Imprimindo os elementos dos índices
arr1[indices] 