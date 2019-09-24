def seleção(v):
  r = []
  while v:
    m = min(v)
    r.append(m)
    v.remove(m)
  return r

def inserção(v):
  for j in range(1, len(v)):
    x = v[j]
    i = j - 1
    while i >= 0 and v[i] > x:
      v[i+1] = v[i]
      i = i - 1
    v[i + 1] = x
  return v

def mergesort(v):
    if len(v) <= 1: return v
    else:
        m = len(v) // 2
        e = mergesort(v[:m])
        d = mergesort(v[m:])
        return merge(e, d)

def merge(e, d):
    r = []
    i, j = 0, 0
    while i < len(e) and j < len(d):
        if e[i] <= d[j]:
            r.append(e[i])
            i += 1
        else:
            r.append(d[j])
            j += 1
    r += e[i:]
    r += d[j:]
    return r

def quicksort(v):
    if len(v) <= 1: return v
    
    pivô = v[0]
    iguais  = [x for x in v if x == pivô]
    menores = [x for x in v if x <  pivô]
    maiores = [x for x in v if x >  pivô]
    return quicksort(menores) + iguais + quicksort(maiores)

cont = 0
def busca_binaria(x, v):
  global cont
  e = -1
  d = len(v)
  while e < d-1:
    m = (e + d) // 2
    cont = cont + 1
    if v[m] < x:
      e = m
    else:
      d = m
  return d

def busca_sequencial(v, x):
    for i in range(len(v)):
        if v[i] == x:
            return True
    return False



from random import sample
from random import randint
import time

dash1 = 42 * '-'
dash2 = 114 * '-'
dash3 = 13 * '-'
dash4 = 48 * '-'
dash5 = 47 * '-'

print('|', dash1,'[EP 1 - Tabela de Ordenação]', dash1,'|')
print('|\tAluno: Daniel Leonard - 3-ADS A\t\t\t\t\t\t\t\t\t\t     |')
print('|\tAluno: Jefferson de Moura - 3-ADS A\t\t\t\t\t\t\t\t\t     |')
print('|', dash2,'|')
print('|\t\t\t\t Tempo de ordenação\t\t\t\tNumero de buscas\t\t     |')
print('|', dash2,'|')
print('|\tn\t| Inserção\tSeleção\tMerge\tQuick\tsortNativo | Inserção\tSeleção\tMerge\tQuick\tsortNativo   |')
print('|', dash3, '|', dash4,'|', dash5, '|')
i = 1
while i <= 5:
    n = 5000 * i
    i += 1
    vetor = sample(range(n), n)


    inicioInsercao = time.time()
    resultadoInsercao = vetor[:]
    resultadoInsercao = inserção(resultadoInsercao)
    fimInsercao = time.time()
    tempoInsercao = fimInsercao - inicioInsercao

    cont_I = 0
    tempo_Total_I = 0
    while tempo_Total_I <= tempoInsercao:
      cont_I += 1
      r = randint(1, n)
      tempo_Sequencial_Inicio = time.time()
      busca_sequencial(vetor, r)
      tempo_Sequencial_Fim = time.time()
      tempo_Sequencial = tempo_Sequencial_Fim - tempo_Sequencial_Inicio
      tempo_Binaria_Inicio = time.time()
      busca_binaria(r, resultadoInsercao)
      tempo_Binaria_Fim = time.time()
      tempo_Binaria = tempo_Binaria_Fim - tempo_Binaria_Inicio
      tempo_Total_I = tempo_Total_I + (tempo_Sequencial - tempo_Binaria)


# tempo_total = 0
# while tempo_total <= tempo_ordenacao:
#   cont = cont + 1
#   r = randint(1, n)
#   t1 = tempo_busca_sequencial
#   t2 = tempo_busca_binaria
#   tempo total = tempo_total + (t1 - t2)


    inicioSelecao = time.time()
    resultadoSelecao = vetor[:]
    resultadoSelecao = seleção(resultadoSelecao)
    fimSelecao = time.time()
    tempoSelecao = fimSelecao - inicioSelecao

    cont_S = 0
    tempo_Total_S = 0
    while tempo_Total_S <= tempoSelecao:
      cont_S += 1
      r = randint(1, n)
      tempo_Sequencial_Inicio = time.time()
      busca_sequencial(vetor, r)
      tempo_Sequencial_Fim = time.time()
      tempo_Sequencial = tempo_Sequencial_Fim - tempo_Sequencial_Inicio
      tempo_Binaria_Inicio = time.time()
      busca_binaria(r, resultadoInsercao)
      tempo_Binaria_Fim = time.time()
      tempo_Binaria = tempo_Binaria_Fim - tempo_Binaria_Inicio
      tempo_Total_S = tempo_Total_S + (tempo_Sequencial - tempo_Binaria)
    

    inicioMergesort = time.time()
    resultadoMergesort = vetor[:]
    resultadoMergesort = mergesort(resultadoMergesort)
    fimMergesort = time.time()
    tempoMergesort = fimMergesort - inicioMergesort

    cont_M = 0
    tempo_Total_M = 0
    while tempo_Total_M <= tempoSelecao:
      cont_M += 1
      r = randint(1, n)
      tempo_Sequencial_Inicio = time.time()
      busca_sequencial(vetor, r)
      tempo_Sequencial_Fim = time.time()
      tempo_Sequencial = tempo_Sequencial_Fim - tempo_Sequencial_Inicio
      tempo_Binaria_Inicio = time.time()
      busca_binaria(r, resultadoInsercao)
      tempo_Binaria_Fim = time.time()
      tempo_Binaria = tempo_Binaria_Fim - tempo_Binaria_Inicio
      tempo_Total_M = tempo_Total_M + (tempo_Sequencial - tempo_Binaria)

    
    inicioQuicksort = time.time()
    resultadoQuicksort = vetor[:]
    resultadoQuicksort = quicksort(resultadoQuicksort)
    fimQuicksort = time.time()
    tempoQuicksort = fimQuicksort - inicioQuicksort

    cont_Q = 0
    tempo_Total_Q = 0
    while tempo_Total_Q <= tempoSelecao:
      cont_Q += 1
      r = randint(1, n)
      tempo_Sequencial_Inicio = time.time()
      busca_sequencial(vetor, r)
      tempo_Sequencial_Fim = time.time()
      tempo_Sequencial = tempo_Sequencial_Fim - tempo_Sequencial_Inicio
      tempo_Binaria_Inicio = time.time()
      busca_binaria(r, resultadoInsercao)
      tempo_Binaria_Fim = time.time()
      tempo_Binaria = tempo_Binaria_Fim - tempo_Binaria_Inicio
      tempo_Total_Q = tempo_Total_Q + (tempo_Sequencial - tempo_Binaria)

    
    InicioSortnativo = time.time()
    resultadoSortnativo = vetor[:]
    resultadoSortnativo.sort()
    fimSortnativo = time.time()
    tempoSortnativo = fimSortnativo - InicioSortnativo

    cont_Sn = 0
    tempo_Total_Sn = 0
    while tempo_Total_Sn <= tempoSelecao:
      cont_Sn += 1
      r = randint(1, n)
      tempo_Sequencial_Inicio = time.time()
      busca_sequencial(vetor, r)
      tempo_Sequencial_Fim = time.time()
      tempo_Sequencial = tempo_Sequencial_Fim - tempo_Sequencial_Inicio
      tempo_Binaria_Inicio = time.time()
      busca_binaria(r, resultadoInsercao)
      tempo_Binaria_Fim = time.time()
      tempo_Binaria = tempo_Binaria_Fim - tempo_Binaria_Inicio
      tempo_Total_Sn = tempo_Total_Sn + (tempo_Sequencial - tempo_Binaria)
      
    print(f'|\t{n}\t| {tempoInsercao:.4f}     \t{tempoSelecao:.4f}', end = '')
    print(f'\t{tempoMergesort:.4f}\t{tempoQuicksort:.4f}\t{tempoSortnativo:.4f}\t   |', end = '')
    print(f' {cont_I}\t{cont_S}\t{cont_M}\t{cont_Q}\t{cont_Sn}\t     |')
print('|', dash2,'|')
