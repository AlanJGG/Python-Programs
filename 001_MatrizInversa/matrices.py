import numpy as np
from fractions import Fraction

def llenarMatriz(dim: int):
    mat = []
    for i in range(dim):
        row = []
        print("Ingresa la fila ", i+1)
        for j in range(dim):
            row.append(int(input()))
        mat.append(row)
    return np.array(mat, dtype=float)

def llenarMatrizIdentidad(dim: int):
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
    #Calcula el determinante de la matriz, si este es 0 no tiene inversa y devuelve False
    if np.linalg.det(matriz) == 0:
        return False
    else:
        return True

def flotanteAFraccion(mat, dim):
    matriz_fraccion = np.empty_like(mat, dtype=object)  # Matriz vacía para almacenar fracciones
    for i in range(dim):
        for j in range(dim):
            matriz_fraccion[i][j] = Fraction(str(mat[i][j])).limit_denominator()  # Convertir a fracción y almacenar en la matriz
    return matriz_fraccion  # Retornar la matriz convertida a fracciones


def gaussJordan(mat, matIdentidad, dim):
    #Llevar a gauss
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
    
    #Llevar a gauss jordan
    for i in range(dim - 1, -1, -1):
        for k in range(i - 1, -1, -1):
            factor = mat[k][i]  # Factor por el que se debe multiplicar la fila i
            mult_factor = mat[i][i] * factor  # Multiplicación de la fila i por el factor
            mult_factor_inv = matIdentidad[i][i] * factor  # Multiplicación de la fila i de la inversa por el factor
            for j in range(dim):
                mat[k][j] = mat[k][j] - (mat[i][j] * factor)  # Resta de la fila k multiplicada por el factor
                matIdentidad[k][j] = matIdentidad[k][j] - (matIdentidad[i][j] * factor)  # Resta de la fila k de la inversa multiplicada por el factor
    
    mat.tolist()
    matIdentidad.tolist()


