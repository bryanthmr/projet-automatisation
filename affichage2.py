import networkx as nx
import matplotlib.pyplot as plt
import csv

def afficher_automate(csv_file):
    G = nx.DiGraph()

    # Lire le fichier CSV et ajouter les transitions au graphe
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Ignorer la première ligne
        for row in reader:
            if len(row) == 3:
                G.add_edge(row[0], row[1], label=row[2])

    # Ajouter des attributs aux nœuds pour les états initiaux et finaux
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Ignorer la première ligne
        for row in reader:
            if len(row) == 2:
                if row[0] == 'État Initial':
                    G.nodes[row[1]]['initial'] = True
                elif row[0] == 'État Final':
                    G.nodes[row[1]]['final'] = True

    # Dessiner le graphe
    pos = nx.circular_layout(G)  # Ajustez l'algorithme de disposition si nécessaire
    labels = nx.get_edge_attributes(G, 'label')
    initial_states = [node for node, data in G.nodes(data=True) if 'initial' in data and data['initial']]
    final_states = [node for node, data in G.nodes(data=True) if 'final' in data and data['final']]

    nx.draw_networkx_nodes(G, pos, node_size=1000, node_color="skyblue", nodelist=initial_states)
    nx.draw_networkx_nodes(G, pos, node_size=1000, node_color="salmon", nodelist=final_states)
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color="lightgray", nodelist=set(G.nodes) - set(initial_states + final_states))
    
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)

    edge_labels = {(u, v): labels[(u, v)] for u, v in G.edges}
    edge_label_pos = {k: (v[0], v[1] + 0.1) for k, v in pos.items()}  # Ajuster la position en y
    nx.draw_networkx_edge_labels(G, edge_label_pos, edge_labels=edge_labels)

    plt.show()

# Utilisation du code
csv_file_path = 'csv/test5.csv'  # Remplacez par le chemin de votre fichier CSV
afficher_automate(csv_file_path)
