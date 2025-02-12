from graphviz import Digraph

# Création de l'arbre avec Graphviz
def creer_arbre():
    dot = Digraph()

    # Ajout des noeuds
    dot.node('N0', '-')  # Racine
    dot.node('N1', '/')  # Sous-arbre gauche
    dot.node('N2', '+')  # Sous-arbre droit

    dot.node('N3', '*')  # Sous-arbre gauche du '/'
    dot.node('N4', '+')  # Sous-arbre droit du '/'

    dot.node('N5', '+')
    dot.node('N6', '3')

    dot.node('N7', '3')
    dot.node('N8', '1')

    dot.node('N9', '-')
    dot.node('N10', '2')

    dot.node('N11', '9')  # Sous-arbre gauche du '+'
    dot.node('N12', '5')

    dot.node('N13', '*')
    dot.node('N14', '6')

    dot.node('N15', '3')
    dot.node('N16', '-')

    dot.node('N17', '7')
    dot.node('N18', '4')

    # Création des arêtes (liens entre les noeuds)
    dot.edge('N0', 'N1')  # Lien entre '-' et '/'
    dot.edge('N0', 'N2')  # Lien entre '-' et '+'

    dot.edge('N1', 'N3')  # Lien entre '/' et '*'
    dot.edge('N1', 'N4')  # Lien entre '/' et '+'

    dot.edge('N3', 'N5')  # Lien entre '*' et '3'
    dot.edge('N3', 'N6')  # Lien entre '*' et '1'

    dot.edge('N5', 'N7')  # Lien entre '*' et '3'
    dot.edge('N5', 'N8')  # Lien entre '*' et '1'

    dot.edge('N4', 'N9')  # Lien entre '+' et '5'
    dot.edge('N4', 'N10') # Lien entre '+' et '2'

    dot.edge('N9', 'N11')  # Lien entre '+' et '5'
    dot.edge('N9', 'N12') # Lien entre '+' et '2'

    dot.edge('N2', 'N13')  # Lien entre '+' et '*'
    dot.edge('N2', 'N14')  # Lien entre '+' et '6'

    dot.edge('N13', 'N15')  # Lien entre '*' et '3'
    dot.edge('N13', 'N16')  # Lien entre '*' et '-'

    dot.edge('N16', 'N17')  # Lien entre '7' et '4'
    dot.edge('N16', 'N18')  # Lien entre '7' et '4'

    # Sauvegarder et afficher l'arbre
    dot.render('arbre', format='pdf', cleanup=True)
    print("Arbre généré avec succès.")

    return dot  # Retourne le graphe pour d'autres utilisations

def inorder_traversal(node):
    """Effectue un parcours Inorder."""
    return inorder_traversal(node.left) + [node.value] + inorder_traversal(node.right) if node else []

def preorder_traversal(node):
    """Effectue un parcours Preorder."""
    return [node.value] + preorder_traversal(node.left) + preorder_traversal(node.right) if node else []

def postorder_traversal(node):
    """Effectue un parcours Postorder."""
    return postorder_traversal(node.left) + postorder_traversal(node.right) + [node.value] if node else []

# Représentation de l'arbre en mémoire
class NodeMemory:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def construire_arbre():
    """Construit l'arbre en mémoire."""
    root = NodeMemory('-')
    root.left = NodeMemory('/')
    root.right = NodeMemory('+')

    root.left.left = NodeMemory('*')
    root.left.right = NodeMemory('+' )

    root.left.left.left = NodeMemory('+')
    root.left.left.right = NodeMemory('3')

    root.left.left.left.left= NodeMemory("3")
    root.left.left.left.right= NodeMemory("1")

    root.left.right.left = NodeMemory('-')
    root.left.right.right = NodeMemory('2')

    root.left.right.left.left = NodeMemory('9')
    root.left.right.left.right = NodeMemory('5')

    root.right.left = NodeMemory('*')
    root.right.right = NodeMemory('6')

    root.right.left.left = NodeMemory('3')
    root.right.left.right = NodeMemory('-')

    root.right.left.right.left = NodeMemory('7')
    root.right.left.right.right = NodeMemory('4')  
    return root

if __name__ == "__main__":
    # Création de l'arbre et génération du graphe
    dot = creer_arbre()
    
    # Construction de l'arbre en mémoire
    arbre_en_memoire = construire_arbre()

    # Traversées
    inorder = inorder_traversal(arbre_en_memoire)
    preorder = preorder_traversal(arbre_en_memoire)
    postorder = postorder_traversal(arbre_en_memoire)

    print("Inorder:", inorder)
    print("Preorder:", preorder)
    print("Postorder:", postorder)

   
    dot.view()  # Affiche le graphique
