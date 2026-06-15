
class Node:
    def __init__(self,key):
        self.right =None
        self.left =None
        self.val=key
        

def inOrder(node):
    if node is None:
        return
        
    inOrder(node.left)
    print(f" {node.val} -> ")
    inOrder(node.right)
        

      
    
    
    
        
if __name__ == "__main__":
    
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    
    
    
    inOrder(root)