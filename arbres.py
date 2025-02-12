from graphviz import Digraph

# Create the tree using Graphviz
def create_tree():
    dot = Digraph()

    # Adding nodes
    dot.node('N0', '-')  # Root
    dot.node('N1', '/')  # Left subtree
    dot.node('N2', '+')  # Right subtree

    dot.node('N3', '*')  # Left subtree of '/'
    dot.node('N4', '+')  # Right subtree of '/'

    dot.node('N5', '+')
    dot.node('N6', '3')

    dot.node('N7', '3')
    dot.node('N8', '1')

    dot.node('N9', '-')
    dot.node('N10', '2')

    dot.node('N11', '9')  # Left subtree of '+'
    dot.node('N12', '5')

    dot.node('N13', '*')
    dot.node('N14', '6')

    dot.node('N15', '3')
    dot.node('N16', '-')

    dot.node('N17', '7')
    dot.node('N18', '4')

    # Creating edges (links between nodes)
    dot.edge('N0', 'N1')  # Link between '-' and '/'
    dot.edge('N0', 'N2')  # Link between '-' and '+'

    dot.edge('N1', 'N3')  # Link between '/' and '*'
    dot.edge('N1', 'N4')  # Link between '/' and '+'

    dot.edge('N3', 'N5')  # Link between '*' and '3'
    dot.edge('N3', 'N6')  # Link between '*' and '1'

    dot.edge('N5', 'N7')  # Link between '*' and '3'
    dot.edge('N5', 'N8')  # Link between '*' and '1'

    dot.edge('N4', 'N9')  # Link between '+' and '5'
    dot.edge('N4', 'N10') # Link between '+' and '2'

    dot.edge('N9', 'N11')  # Link between '+' and '5'
    dot.edge('N9', 'N12') # Link between '+' and '2'

    dot.edge('N2', 'N13')  # Link between '+' and '*'
    dot.edge('N2', 'N14')  # Link between '+' and '6'

    dot.edge('N13', 'N15')  # Link between '*' and '3'
    dot.edge('N13', 'N16')  # Link between '*' and '-'

    dot.edge('N16', 'N17')  # Link between '7' and '4'
    dot.edge('N16', 'N18')  # Link between '7' and '4'

    # Save and display the tree
    dot.render('tree', format='pdf', cleanup=True)
    print("Tree successfully generated.")

    return dot  # Returns the graph for further use

# Tree traversal functions
def inorder_traversal(node):
    """Performs an inorder traversal."""
    return inorder_traversal(node.left) + [node.value] + inorder_traversal(node.right) if node else []

def preorder_traversal(node):
    """Performs a preorder traversal."""
    return [node.value] + preorder_traversal(node.left) + preorder_traversal(node.right) if node else []

def postorder_traversal(node):
    """Performs a postorder traversal."""
    return postorder_traversal(node.left) + postorder_traversal(node.right) + [node.value] if node else []

# Memory representation of the tree
class NodeMemory:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def construct_tree():
    """Builds the tree in memory."""
    root = NodeMemory('-')
    root.left = NodeMemory('/')
    root.right = NodeMemory('+')

    root.left.left = NodeMemory('*')
    root.left.right = NodeMemory('+')

    root.left.left.left = NodeMemory('+')
    root.left.left.right = NodeMemory('3')

    root.left.left.left.left = NodeMemory("3")
    root.left.left.left.right = NodeMemory("1")

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
    # Create and generate the graph
    dot = create_tree()
    
    # Build the tree in memory
    tree_in_memory = construct_tree()

    # Tree traversals
    inorder = inorder_traversal(tree_in_memory)
    preorder = preorder_traversal(tree_in_memory)
    postorder = postorder_traversal(tree_in_memory)

    print("Inorder Traversal:", inorder)
    print("Preorder Traversal:", preorder)
    print("Postorder Traversal:", postorder)

    # Display the graph
    dot.view()
