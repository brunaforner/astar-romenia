# -*- coding: utf-8 -*-
# fase2_caminhos.py — Fase 2: funções, custo de um caminho e os valores g, h e f.
# Rode com: python fase2_caminhos.py

# ----- PASSO 1: importar os dados -----

from mapa import mapa_romenia, heuristica_bucareste

# ----- PASSO 2: função que devolve o custo de UMA estrada -----

def custo_da_estrada(origem, destino):
    """Devolve os km da estrada origem -> destino, ou None se ela não existe."""
    for vizinho, custo in mapa_romenia[origem]:
        if vizinho == destino:
            return custo
    return None

# ----- PASSO 3: função que soma o custo de um caminho inteiro -----

def custo_do_caminho(caminho):
    """Recebe uma lista de cidades e devolve a soma das estradas, em km."""
    total = 0
    for i in range(len(caminho) - 1):
        total = total + custo_da_estrada(caminho[i], caminho[i + 1])
    return total

# ----- PASSO 4: testar as funções -----

print('Arad -> Sibiu custa', custo_da_estrada('Arad', 'Sibiu'), 'km')
print('Arad -> Bucharest custa', custo_da_estrada('Arad', 'Bucharest'),
 '(não existe estrada direta)')

por_fagaras = ['Arad', 'Sibiu', 'Fagaras', 'Bucharest']
por_pitesti = ['Arad', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti', 'Bucharest']
print()
print('Caminho por Fagaras:', ' -> '.join(por_fagaras))
print(' custo =', custo_do_caminho(por_fagaras), 'km')
print('Caminho por Pitesti:', ' -> '.join(por_pitesti))
print(' custo =', custo_do_caminho(por_pitesti), 'km')
