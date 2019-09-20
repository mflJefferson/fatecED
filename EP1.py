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

from random import sample
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
    inserção(resultadoInsercao)
    fimInsercao = time.time()
    tempoInsercao = fimInsercao - inicioInsercao

    
    inicioSelecao = time.time()
    resultadoSelecao = vetor[:]
    resultadoSelecao = seleção(resultadoSelecao)
    fimSelecao = time.time()
    tempoSelecao = fimSelecao - inicioSelecao
    

    inicioMergesort = time.time()
    resultadoMergesort = vetor[:]
    resultadoMergesort = mergesort(resultadoMergesort)
    fimMergesort = time.time()
    tempoMergesort = fimMergesort - inicioMergesort

    
    inicioQuicksort = time.time()
    resultadoQuicksort = vetor[:]
    resultadoQuicksort = quicksort(resultadoQuicksort)
    fimQuicksort = time.time()
    tempoQuicksort = fimQuicksort - inicioQuicksort

    
    InicioSortnativo = time.time()
    resultadoSortnativo = vetor[:]
    resultadoSortnativo.sort()
    fimSortnativo = time.time()
    tempoSortnativo = fimSortnativo - InicioSortnativo

    placeholder = 0000
    print(f'|\t{n}\t| {tempoInsercao:.4f}     \t{tempoSelecao:.4f}', end = '')
    print(f'\t{tempoMergesort:.4f}\t{tempoQuicksort:.4f}\t{tempoSortnativo:.4f}\t   |', end = '')
    print(f' {placeholder}\t\t{placeholder}\t{placeholder}\t{placeholder}\t{placeholder}\t     |')
print('|', dash2,'|')