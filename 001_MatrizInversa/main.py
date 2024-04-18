from matrices import *

dim = int(input("Ingresa la dimensión de la matriz: "))

mat = llenarMatriz(dim)
matIdentidad = llenarMatrizIdentidad(dim)
if tieneInversa(mat):
    print("\n--Matriz Inicial e Identidad--\n")
    imprimirMatrices(mat, matIdentidad, dim)
    gaussJordan(mat, matIdentidad, dim)
    print("\n--Matriz Resultante e Inversa--\n")
    #imprimirMatrices(mat, matIdentidad, dim)
    imprimirMatrices(flotanteAFraccion(mat, dim), flotanteAFraccion(matIdentidad, dim), dim)
else:
    print("\nLa matriz no tiene inversa\n")
            