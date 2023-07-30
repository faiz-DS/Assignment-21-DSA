class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect_nodes_at_same_level(root):
    if not root:
        return

    # Initialize the queue for level-order traversal
    queue = [root]

    while queue:
        level_size = len(queue)
        prev_node = None

        for i in range(level_size):
            current_node = queue.pop(0)

            # Connect the current node to the previous node at the same level
            if prev_node:
                prev_node.next = current_node

            # Update the previous node to the current node
            prev_node = current_node

            # Add the children of the current node to the queue
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        # Set the "next" pointer of the last node in the level to None
        prev_node.next = None

# Helper function to print the connected nodes
def print_connected_nodes(root):
    current = root
    while current:
        print(current.val, end=" → ")
        current = current.next
    print("-1")

# Given binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Connect nodes at the same level
connect_nodes_at_same_level(root)

# Print the connected nodes at each level
print_connected_nodes(root)
print_connected_nodes(root.left)
print_connected_nodes(root.left.left)

"""output
(1 → -1
2 → 3 → -1
4 → 5 → 6 → 7 → -1
)"""