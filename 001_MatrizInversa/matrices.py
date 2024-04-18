import numpy as np
from fractions import Fraction

def llenarMatriz(dim: int):
    #Pide los datos para llenar una matriz y devolverla.
    mat = []
    for i in range(dim):
        row = []
        print("Ingresa la fila ", i+1)
        for j in range(dim):
            row.append(int(input()))
        mat.append(row)
    return np.array(mat, dtype=float)

def llenarMatrizIdentidad(dim: int):
    #Devuelve una matriz identidad nxn.
    mat = []
    for i in range(dim):
        row = []
        for j in range(dim):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        mat.append(row)
    return np.array(mat, dtype=float)

def imprimirMatrices(mat, matIdentidad, dim: int):
    #Imprime la matriz y matriz identidad.
    for i in range(dim):
        print('|', end=' ')
        for j in range(dim):
            print(mat[i][j], end=' ')
        print('|', end=' ')
        
        for k in range(dim):
            print(matIdentidad[i][k], end=' ')
        print('|')
    print()

def tieneInversa(matriz):
    #Calcula el determinante de la matriz, si este es 0 quiere decir que no tiene inversa y devuelve False.
    if np.linalg.det(matriz) == 0:
        return False
    else:
        return True

def flotanteAFraccion(mat, dim):
    #Devuelve una matriz de fracciones tras recibir una matriz de numeros flotantes o enteros.
    matriz_fraccion = np.empty_like(mat, dtype=object)
    for i in range(dim):
        for j in range(dim):
            matriz_fraccion[i][j] = Fraction(str(mat[i][j])).limit_denominator()
    return matriz_fraccion


def gaussJordan(mat, matIdentidad, dim):
    #Lleva la matriz a su forma gaussiana.
    for i in range(dim):
        aux = mat[i][i]
        for j in range(dim):
            mat[i][j] = mat[i][j] / aux
            matIdentidad[i][j] = matIdentidad[i][j] / aux
        
        #Hace ceros los elementos debajo del 1 principal
        for k in range(dim):
            if k != i:
                factor = mat[k][i]
                for j in range(dim):
                    mat[k][j] = mat[k][j] - (mat[i][j] * factor)
                    matIdentidad[k][j] = matIdentidad[k][j] - (matIdentidad[i][j] * factor)
    
    #Lleva la matriz a gauss-jordan.
    for i in range(dim - 1, -1, -1):
        for k in range(i - 1, -1, -1):
            factor = mat[k][i]
            mult_factor = mat[i][i] * factor 
            mult_factor_inv = matIdentidad[i][i] * factor
            #Vuelve ceros el triangulo superior de la matriz.
            for j in range(dim):
                mat[k][j] = mat[k][j] - (mat[i][j] * factor)
                matIdentidad[k][j] = matIdentidad[k][j] - (matIdentidad[i][j] * factor) 
    
    mat.tolist()
    matIdentidad.tolist()


