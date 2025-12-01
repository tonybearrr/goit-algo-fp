"""Binary tree traversal visualization: DFS and BFS."""
import uuid
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    """Node in binary tree"""
    def __init__(self, key, color="skyblue"):
        """Initialize node with key, color and unique identifier"""
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """Add edges to graph for visualization"""
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
    if node.left:
        graph.add_edge(node.id, node.left.id)
        l = x - 1 / 2 ** layer
        pos[node.left.id] = (l, y - 1)
        add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
    if node.right:
        graph.add_edge(node.id, node.right.id)
        r = x + 1 / 2 ** layer
        pos[node.right.id] = (r, y - 1)
        add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, title="Binary Tree"):
    """Visualize binary tree"""
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.title(title)
    plt.show()


def generate_color(step, total):
    """Generate color from dark to light based on step"""
    ratio = step / total
    r = int(0 + (135 - 0) * ratio)
    g = int(100 + (206 - 100) * ratio)
    b = int(200 + (235 - 200) * ratio)
    return f"#{r:02x}{g:02x}{b:02x}"


def dfs(root):
    """Depth-First Search using explicit stack"""
    if root is None:
        return []

    visited_order = []
    stack = [root]
    while stack:
        node = stack.pop()
        visited_order.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return visited_order


def bfs(root):
    """Breadth-First Search using queue"""
    if root is None:
        return []
    visited_order = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        visited_order.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return visited_order


def reset_colors(root):
    """Reset all node colors to default"""
    if root is None:
        return
    root.color = "skyblue"
    reset_colors(root.left)
    reset_colors(root.right)


if __name__ == "__main__":
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    # DFS обхід
    print("DFS обхід (у глибину):")
    dfs_order = dfs(root)
    dfs_values = [node.val for node in dfs_order]
    print(f"Послідовність: {dfs_values}")

    total_nodes = len(dfs_order)
    for idx, node in enumerate(dfs_order):
        node.color = generate_color(idx, total_nodes)

    draw_tree(root, "DFS обхід (у глибину)")

    # Скидаємо кольори
    reset_colors(root)

    # BFS обхід
    print("\nBFS обхід (в ширину):")
    bfs_order = bfs(root)
    bfs_values = [node.val for node in bfs_order]
    print(f"Послідовність: {bfs_values}")

    total_nodes = len(bfs_order)
    for idx, node in enumerate(bfs_order):
        node.color = generate_color(idx, total_nodes)

    draw_tree(root, "BFS обхід (в ширину)")
