from typing import Dict

votaram: Dict[str, bool] = {}


def verifica_eleitor(nome: str):
    if votaram.get(nome):
        print("Mande Embora !")
    else:
        votaram[nome] = True
        print("Deixe votar !")


verifica_eleitor("Tom")  # Deixe votar !
verifica_eleitor("Mike")  # Deixe votar !
verifica_eleitor("Mike")  # Mande Embora !
