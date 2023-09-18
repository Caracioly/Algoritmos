def soma(lista):
    if not lista:
        return 0
    primeiro_numero = lista.pop()
    return primeiro_numero + soma(lista)


def soma2(lista):
    if lista == []:
        return 0
    return lista[0] + soma2(lista[1:])


print(soma2([5, 10, 15, 20]))


def lentgh(lista):
    if not lista:
        return 0
    else:
        return 1 + lentgh(lista[1:])


print(lentgh([3, 4, 5, 6, 7, 8]))


def get_maior_valor(lista):
    maior_numero = 0
    if not lista:
        return 0
    else:
        for i in lista:
            if i > maior_numero:
                maior_numero = i
        return maior_numero


def maximo(lista):
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]
    sub_max = maximo(lista[1:])
    return lista[0] if lista[0] > sub_max else sub_max


print(get_maior_valor([3, 1, 10, 13, 56, 32]))
print(f"maximo: {maximo([3, 1, 10, 13, 56, 32])}")


def quickSort(array):
    if len(array) < 2:
        return array
    pivo = array[0]
    menores = [i for i in array[1:] if i <= pivo]
    maiores = [i for i in array[1:] if i > pivo]
    return quickSort(menores) + [pivo] + quickSort(maiores)


print(f"quicksort: {quickSort([33, 15, 10, 5, 2, 3])}")


def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = round((baixo + alto) / 2)
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    raise ValueError(f"Elemento {item} não foi encontrado na lista.")


minha_lista = [1, 3, 5, 7, 9]
try:
    print(pesquisa_binaria(minha_lista, 3))  # -> maior que 1
    print(pesquisa_binaria(minha_lista, 50))  # -> none
except ValueError as e:
    print(e)


def busca_menor(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice


def ordenacao_por_Selecao(arr):
    novo_arr = []
    for i in range(len(arr)):
        menor = busca_menor(arr)
        novo_arr.append(arr.pop(menor))
    return novo_arr


print(ordenacao_por_Selecao([5, 3, 6, 2, 10]))


def fat(x):
    if x <= 1:
        return 1
    return x * fat(x - 1)


print(f"Fatorial é {fat(5)}")

