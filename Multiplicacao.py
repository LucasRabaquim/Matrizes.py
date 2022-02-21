def Matriz(Letra):
    print("\nMatriz " + Letra + "\n")
    Matriz = []
    ordemM = int(input("Digite a ordem n: "))
    ordemN = int(input("Digite a ordem m: "))
    for i in range(ordemM): 
        Matriz.append([])
        for j in range(ordemN) : 
            Matriz[i].append(int(input(Letra.lower() +str(i+1)+str(j+1)+": ")))
    Formatar(Matriz)
    return Matriz,ordemM,ordemN

def Multiplicar(A,B):
    MatrizC = []
    for i in range(A[1]):
        for j in range(B[2]):
            c = 0 
            for coluna in range(len(A[0])):
                c += (A[0][i][coluna]) * (B[0][coluna][j])
            MatrizC.append(c)
    return MatrizC

def Formatar(matriz):
    for i in range (len(matriz)):
        print(matriz[i])

MatrizA = Matriz("A")
MatrizB = Matriz("B")
MatrizC = Multiplicar(MatrizA,MatrizB)
print(f'\n {MatrizC}')