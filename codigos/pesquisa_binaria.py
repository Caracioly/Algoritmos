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
    pesquisa_binaria(minha_lista, 3)  # -> maior que 1
    pesquisa_binaria(minha_lista, 50)  # -> none
except ValueError as e:
    print(e)
