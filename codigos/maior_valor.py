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
