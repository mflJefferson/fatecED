# def enumerações(items):
#     n = len(items)
#     s = [0]*(n+1)
#     k = 0
#     while True:
#         if s[k] < n:
#             s[k+1] = s[k] + 1
#             k += 1
#         else:
#             s[k-1] += 1
#             k -= 1
#         if k == 0: break
#         else:
#             lista = []
#             for j in range(1, k+1):
#                 lista.append(items[s[j]-1])
#             yield lista

# def combinações(items, n):
#     if n==0: yield []
#     else:
#         for i in range(len(items)):
#             for cc in combinações(items[:i]+items[i+1:],n-1):
#                 yield [items[i]]+cc

# def permutações(items):
#     return combinações(items, len(items))

# for p in permutações(['Adriano','Bruno', 'Diogo', 'Eclis', 'Gabriel', 'Leandro', 'Walber']):
#     print (p)

# for p in enumerações(['Jessica', 'Fernanda', 'Pamela', 'Renata']):
#     print (p)

# c = ["Adriano", "Bruno", "Leandro", "Gabriel", "Diogo", "Eclis", "Walber"]

# print ('Permutações')
# for p in permutações([1, 2, 3]):
#    print (p)

# for p in permutações(c):
#     print(p)

# for p in enumerações(c):
#     print(p)

# print ('Enumerações')
# for p in enumerações([, 2, 3]):
#    print (p)

c1 = ["Adriano", "Bruno", "Gabriel", "Leandro", "Walber"]
c2 = ["Bruno", "Adriano", "Eclis"]
c3 = ["Diogo", "Eclis", "Gabriel", ]
c4 = ["Eclis", "Bruno", "Diogo"]
c5 = ["Gabriel", "Adriano", "Diogo", "Walber"]
c6 = ["Leandro", "Adriano", "Bruno", "Walber"]
c7 = ["Walber", "Adriano", "Gabriel", "Leandro"]
c8 = []

Cavaleiros = {"Adriano": ["Bruno", "Gabriel", "Leandro", "Walber"],
 "Bruno": ["Adriano", "Eclis"], 
 "Diogo": ["Eclis", "Gabriel"],
 "Eclis": ["Bruno", "Diogo"],
 "Gabriel": ["Adriano", "Diogo", "Walber"],
 "Leandro": ["Adriano", "Bruno", "Walber"],
 "Walber": ["Adriano", "Gabriel", "Leandro"]}

caminho = []
pt = {}

def hamilton(G, size, pt, path = []):
    print('hamilton called with pt={}, path={}'.format(pt, path))
    if pt not in set(path):
        path.append(pt)
        if len(path)==size:
            return path
        for pt_next in G.get(pt, []):
            res_path = [i for i in path]
            candidate = hamilton(G, size, pt_next, res_path)
            if candidate is not None:  # skip loop or dead end
                return candidate
        print('path {} is a dead end'.format(path))
    else:
        print('pt {} already in path {}'.format(pt, path))
    # loop or dead end, None is implicitly returned
hamilton(Cavaleiros, 7, "Adriano", caminho)

# def mesa(lista, nextList):
#     for x in lista:
#         if x in nextList and x not in c8:
#             c8.append(x)


# mesa(c1, c2)
# mesa(c2, c3)
# mesa(c3, c4)
# mesa(c3, c5)
# mesa(c5, c6)
# mesa(c6, c7)
# mesa(c7, c1)
# print(c8)


# problama do circuito hamiltoniano
# passar por todos os pontos sem repetir
# e voltar a origem

# Resolve o problema das damas se as damas forem vértices ímpares
# tenho 2 possibilidades de casar todas (Grafos)
# Problema do emparelhamento máximo


