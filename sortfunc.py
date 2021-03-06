def listGen(tamaño, rango=100):
    import random
    lista = []
    for x in range(tamaño):
        lista.append(random.random() * rango)
    return tuple(lista)


def loadFromFile(name='data.txt', rango=100):
    '''
        Recibe el nombre de un archivo (str)
        Retorna una lista de floats con cada uno
        de los números extraídos del archivo name
    '''
    lista = []
    archivo = open(name, 'r')
    for line in archivo:
        lista.append(listGen(int(line), rango))
    archivo.close()
    return tuple(lista)


def sortBurbuja(Lista):
    ''' Recibe una tupla de floats
        Retorna la cantidad de ciclos (int)
        que se toma el algoritmo de burbuja
        para ordenar la tupla L
    '''
    c = 0
    L = list(Lista)
    tam = len(L)
    for i in range(1, tam):
        for j in range(0, tam - i):
            if(L[j] > L[j + 1]):
                k = L[j + 1]
                L[j + 1] = L[j]
                L[j] = k
            c += 1
    return c
def sortSeleccion(Lista):
    ''' Recibe una lista de floats
        Retorna la cantidad de ciclos (int)
        que se toma el algoritmo de selección
        para ordenar la lista L
    '''
    L = list(Lista)
    tam = len(L)
    c = 0
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if L[i] > L[j]:
                i = j
            c += 1
        aux = L[i]
        L[i] = L[i]
        L[i] = aux
    return c
