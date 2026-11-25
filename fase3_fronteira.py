# -*- coding: utf-8 -*-
# fase3_fronteira.py — Fase 3: o nó de busca e a fronteira, feitos à mão.
# Rode com: python fase3_fronteira.py

# ----- PASSO 1: importar os dados -----

from mapa import mapa_romenia, heuristica_bucareste

# ----- PASSO 2: montar o nó inicial e a fronteira -----
# Um nó é uma tupla com 4 posições: (f, g, cidade, caminho)

inicio = 'Arad'
g = 0
h = heuristica_bucareste[inicio]
no_inicial = (g + h, g, inicio, [inicio])

fronteira = [no_inicial]
print('Fronteira no começo:', fronteira)


# ----- PASSO 3: tirar o primeiro nó da fronteira -----

no = fronteira.pop(0)
f_atual, g_atual, cidade_atual, caminho = no
print()
print('Nó retirado:', no)
print(' f =', f_atual, '| g =', g_atual, '| cidade =', cidade_atual,
 '| caminho =', caminho)
print('Fronteira agora:', fronteira)
