# -*- coding: utf-8 -*-
# fase1_explorar.py — Fase 1: navegar nos dados, sem nenhuma busca ainda.
# Rode com: python fase1_explorar.py

# ----- PASSO 1: trazer os dados do arquivo mapa.py -----

from mapa import mapa_romenia, heuristica_bucareste

# ----- PASSO 2: quantas cidades existem? -----

print('Quantidade de cidades no mapa:', len(mapa_romenia))
print('Quantidade de valores de h(n):', len(heuristica_bucareste))

# ----- PASSO 3: olhar o valor guardado em uma chave -----

vizinhos_arad = mapa_romenia['Arad']
print()
print('Vizinhos de Arad:', vizinhos_arad)
print('Tipo do valor:', type(vizinhos_arad))

# ----- PASSO 4: pegar uma tupla e as partes dela -----

primeira = vizinhos_arad[0]
print()
print('Primeira estrada que sai de Arad:', primeira)
print(' posição [0] -> cidade vizinha:', primeira[0])
print(' posição [1] -> custo em km :', primeira[1])
