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
