import pandas as pd

# Nombres de los nodos con palabras completas
V = ['Hogar', 'Parada_Sidral', 'Estación_ArcosL3', 'Parada_Plaza_Universidad', 'Estación_Plaza_PatriaL3', 'Parada_DQ_Terranova', 'Parada_Parque_Alberta', 'CETI']

# Creamos el DataFrame del grafo
grafo = pd.DataFrame(index=V, columns=V)

# Definimos las conexiones entre los nodos (matriz de adyacencia) (valores en minutos en bicicleta)
grafo.loc['Hogar', ['Parada_Sidral']] = 3
grafo.loc['Hogar', ['Estación_ArcosL3']] = 7
grafo.loc['Parada_Sidral', ['Parada_Plaza_Universidad']] = 31
grafo.loc['Parada_Plaza_Universidad', ['CETI']] = 9
grafo.loc['Estación_ArcosL3', ['Estación_Plaza_PatriaL3']] = 18
grafo.loc['Estación_Plaza_PatriaL3', ['Parada_Parque_Alberta']] = 8
grafo.loc['Estación_Plaza_PatriaL3', ['Parada_DQ_Terranova']] = 12
grafo.loc['Parada_Parque_Alberta', ['CETI']] = 6
grafo.loc['Parada_DQ_Terranova', ['CETI']] = 5


# Rellenamos los valores NaN con 0 (ausencia de conexión)
grafo = grafo.fillna(0)

# Exportar el grafo a JSON
grafo.to_json("grafo.json", orient="split")
grafo.to_json("grafo.json")

# Algoritmo de búsqueda 
V1 = 'CETI'  # Nodo inicial de recorrido
S = [V1]
Vp = [V1]
Ep = []
s = []
d = V.copy()  # Lista de nodos no visitados
d.remove(V1)

while True:
    for x in S:
        # Encuentra nodos adyacentes no visitados
        V = [y for y in d if y in grafo.loc[grafo[x] > 0, x]]
        _ = [(Ep.append((x, y)), Vp.append(y), d.remove(y), s.append(y)) for y in V]
    
    if not s:  # Si no hay nodos nuevos por visitar
        break
    S = s.copy()
    s = []

# Imprime las aristas recorridas y los nodos visitados
print("Aristas recorridas:", Ep)
print("Nodos visitados:", Vp)
