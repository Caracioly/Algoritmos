import json


def carregar_grafo(nome_arquivo, indice_grafo):
    with open(f"codigos/{nome_arquivo}", "r") as arquivo_json:
        lista_de_grafos = json.load(arquivo_json)
    return lista_de_grafos[indice_grafo]


def ache_no_custo_mais_baixo(custos, processados):
    custo_mais_baixo = float("inf")
    nodo_custo_mais_baixo = None
    for nodo in custos:
        if custos[nodo] < custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custos[nodo]
            nodo_custo_mais_baixo = nodo
    return nodo_custo_mais_baixo


def encontrar_caminho_minimo(grafo, inicio, fim):
    infinito = float("inf")
    custos = {nodo: infinito for nodo in grafo}
    pais = {nodo: None for nodo in grafo}
    custos[inicio] = 0
    processados = [list]

    nodo = ache_no_custo_mais_baixo(custos, processados)
    while nodo is not None:
        custo = custos[nodo]
        vizinhos = grafo[nodo]
        for n in vizinhos.keys():
            novo_custo = custo + vizinhos[n]
            if custos[n] > novo_custo:
                custos[n] = novo_custo
                pais[n] = nodo
        processados.append(nodo)
        nodo = ache_no_custo_mais_baixo(custos, processados)

    caminho = [fim]
    nodo_atual = fim
    while nodo_atual != inicio:
        nodo_atual = pais[nodo_atual]
        caminho.append(nodo_atual)

    caminho.reverse()
    return caminho, custos[fim]


grafo = carregar_grafo("grafo.json", 3)["grafo"]

inicio = "inicio"
fim = "fim"

caminho, custo_total = encontrar_caminho_minimo(grafo, inicio, fim)

print(f"Caminho percorrido: {' -> '.join(caminho)}")
print(f"Custo total: {custo_total}")
