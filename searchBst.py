class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_min_max(root):
    # Check if the tree is empty
    if root is None:
        return None, None

    # Find the minimum value (leftmost node)
    min_node = root
    while min_node.left is not None:
        min_node = min_node.left

    # Find the maximum value (rightmost node)
    max_node = root
    while max_node.right is not None:
        max_node = max_node.right

    return min_node.key, max_node.key

# Example usage:

# Create a sample BST
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(12)
root.right.right = TreeNode(18)

# Find the minimum and maximum values
min_value, max_value = find_min_max(root)

print("Minimum value:", min_value)
print("Maximum value:", max_value)
