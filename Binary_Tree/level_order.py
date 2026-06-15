from collections import deque

class Node:
    def __init__(self,value):
        self.left=None
        self.right =None
        self.val=value
        
        
        
 
def LevelOrderTraversal(root,level,res):
    
    #leaf node
    if root is None:
        return 
        
    # create list for new level
    if len(res)<=level:
        res.append([])
        
    #add in level
    res[level].append(root.val)
    
    # traverse to righ and left child
    LevelOrderTraversal(root.left,level+1,res)
    LevelOrderTraversal(root.right,level+1,res)
    
        
    
def levelOrder(root):
    # Stores the result level by level
    res = []
    LevelOrderTraversal(root, 0, res)
    
    for level  in res:
        print(level)
        
        
        
#================ iterative way

def QueueLevelOrderTraversal(root):
    
    
    
    if root is None :
       
        return []
    
    
        
    que=deque()
    #resuslt
    res =[]
    #current level 
    current_level= 0
    que.appendleft(root)
    
    while que:
        
        current_level_node_size = len(que)
        res.append([])
        
        #collect next level node
        for node in range(current_level_node_size):
            node = que.popleft()
            res[current_level].append(node.val)
            
            # travers left + right not
            if node.left is not None:
                que.append(node.left)
            if node.right is not None:
                que.append(node.right)
        
        # encrease level
        current_level+=1
    
    
        
    for x in res:
        print(x)
        
        
        
     
def height(root):
    if root is None:
        return 0
        
    return max(height(root.left),height(root.right))+1
    
        
        
    
                
    
    
if __name__ == '__main__':
    #      5
    #     / \
    #   12   13
    #   /  \    \
    #  7    14    2
    # /  \  /  \  / \
    #17  23 27 3 8  11

    root = Node(5)
    root.left = Node(12)
    root.right = Node(13)

    root.left.left = Node(7)
    root.left.right = Node(14)

    root.right.right = Node(2)

    root.left.left.left = Node(17)
    root.left.left.right = Node(23)

    root.left.right.left = Node(27)
    root.left.right.right = Node(3)

    root.right.right.left = Node(8)
    root.right.right.right = Node(11)

    levelOrder(root)
    
    QueueLevelOrderTraversal(root)
    
    print(f"Height : {height(root)}")
    