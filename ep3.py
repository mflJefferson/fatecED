# matriz de 0s e 1s, só tem ligação de cima para baixo, esquerda, direita.
# LIga aqueles que estão ligados por cima e por baixo
# Diagonal não tem ligação
# Depois de detectar quais pontos estão conectados entre si, renomear os números 1s
# Criar estrutura de dados do tipo lista

# Não entrar com arquivo.

ex1 = '''
010
111
000
101'''

M = [list(linha) for linha in ex1.split()]



#Perguntar se tem 1, perguntar se tem gente em cima ou do lado. Se sim significa que já existe uma região

regiões = []
regiões.append([(0, 1)])
regiões[0].append((1, 1))
regiões[0].append((1, 0))
regiões[0].append((1, 2))
regiões.append([(3, 0)])
regiões.append([(3, 2)])

print(regiões)

ord('1')
count = 49
for r in regiões:
    for x, y in r:
        M[x] [y] = chr(count)
    count = count + 1

for linha in M:
    print(''.join(linha))

ex2 = '''
10101
10101
11111'''

N = [list(linha) for linha in ex2.split()]

regi = []
regi.append([(0, 0)])
regi[0].append((0, 2))
regi[0].append((0, 4))
regi[0].append((1, 0))
regi[0].append((1, 2))
regi[0].append((1, 4))
regi[0].append((2, 0))
regi[0].append((2, 1))
regi[0].append((2, 2))
regi[0].append((2, 3))
regi[0].append((2, 4))
print(regi)
ord('1')
count = 49

for r in regi:
    for x, y in r:
        N[x] [y] = chr(count)
    count = count + 1

for linha in N:
    print(''.join(linha))

ex3 = '''
0011001010
0110001010
0011001110
0000000000
0010001010
0010011111
1111100000
0010001110
0010001110'''

P = [list(linha) for linha in ex3.split()]

regioes3 = []
regioes3.append([(0, 2)])
regioes3[0].append((0, 3))
regioes3[0].append((1, 1))
regioes3[0].append((1, 2))
regioes3[0].append((2, 2))
regioes3[0].append((2, 3))
regioes3.append([(0, 6)])
regioes3[1].append((0, 8))
regioes3[1].append((1, 6))
regioes3[1].append((1, 8))
regioes3[1].append((2, 6))
regioes3[1].append((2, 7))
regioes3[1].append((2, 8))
regioes3.append([(4, 2)])
regioes3[2].append((5, 2))
regioes3[2].append((6, 0))
regioes3[2].append((6, 1))
regioes3[2].append((6, 2))
regioes3[2].append((6, 3))
regioes3[2].append((6, 4))
regioes3[2].append((7, 2))
regioes3[2].append((8, 2))
regioes3.append([(4, 6)])
regioes3[3].append((4, 8))
regioes3[3].append((5, 5))
regioes3[3].append((5, 6))
regioes3[3].append((5, 7))
regioes3[3].append((5, 8))
regioes3[3].append((5, 9))
regioes3.append([(7, 6)])
regioes3[4].append((7, 7))
regioes3[4].append((7, 8))
regioes3[4].append((8, 6))
regioes3[4].append((8, 7))
regioes3[4].append((8, 8))




print(regioes3)



ord('1')
count = 49
for r in regioes3:
    for x, y in r:
        P[x][y] = chr(count)
    count = count +1
for linha in P:
    print(''.join(linha))