def lentgh(lista):
    if not lista:
        return 0
    else:
        return 1 + lentgh(lista[1:])


print(lentgh([3, 4, 5, 6, 7, 8]))
