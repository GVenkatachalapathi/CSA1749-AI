from collections import deque

class TreeNode:
    def __init__(self, value):  
        self.value = value
        self.children = []  

    def add_child(self, child_node):
        self.children.append(child_node)

def bfs(root):
    if root is None:
        return []

    queue = deque([root])  
    result = []  

    while queue:
        current_node = queue.popleft() 
        result.append(current_node.value)  

        for child in current_node.children:
            queue.append(child)

    return result

if __name__ == "__main__": 
    root = TreeNode(1)
    child_a = TreeNode(2)
    child_b = TreeNode(3)
    child_c = TreeNode(4)
    child_d = TreeNode(5)

    root.add_child(child_a)
    root.add_child(child_b)
    child_a.add_child(child_c)
    child_a.add_child(child_d)

    bfs_result = bfs(root)

    print("BFS Traversal Order:", bfs_result)
