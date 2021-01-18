
#matriz A
print('Matriz A ',end='')
fil1=int(input("  Filas: "))
col1=int(input(" Columnas: "))
#matriz B
print('Matriz B ',end='')
fil2=int(input(" Filas: "))
col2=int(input(" Columnas: "))
if col1 == fil2:
    print('Ingrese datos de la matriz A:',end='')
    matrizA = []
    for i in range(fil1):
        matrizA.append( [0] * col1)#append agrega el valor al final del arreglo
    for i in range(fil1):
        for j in range(col1):
            matrizA[i][j]=int(input('A[%d,%d]: '%(i,j)))
    print(' Ingrese datos de la matriz B:',end='')
    matrizB = []
    for i in range(fil2):
        matrizB.append( [0] * col2)
    for i in range(fil2):
        for j in range(col2):
            matrizB[i][j]=int(input('B[%d,%d]: '%(i,j)))
    matrizRes = []
    for i in range(fil1):
        matrizRes.append( [0] * col2)
    for i in range(fil1):
        for j in range(col2):
            acum=0
            for m in range(col1):
                acum=acum+matrizA[i][m]*matrizB[m][j]
                matrizRes[i][j]=acum
    print(' Matriz resultante: ',end='')
    print(matrizRes)
else:
    print(' No se puede realizar la multiplicación')
    