'''
'''
class Node:
    def __init__(self,val,pos):
        self.data = val
        self.left = None
        self.right = None
        self.pos = pos
        
class BST:
    def __init__(self):
        self.root = None
        
    def Insert(self,x):
        self.InsertHelper(self.root,1,x)
    
    def InsertHelper(self,Root,pos,x):
        if Root ==None: 
            Root = Node(x,pos)
            print(pos)
            self.root = Root
        else:
            if x<=Root.data:
                if Root.left!=None:
                    self.InsertHelper(Root.left,2*pos,x)
                else:
                    Root.left=Node(x,2*pos)
                    print(Root.left.pos)
            else:
                if Root.right!=None:
                    self.InsertHelper(Root.right,2*pos+1,x)
                else:
                    Root.right=Node(x,2*pos+1)
                    print(Root.right.pos)
    
    def Search(self,x,Root = -1):
        if Root == -1:
            Root = self.root
        if Root == None:return
        elif Root.data == x:return Root
        elif Root.data < x :return self.Search(x,Root.right)
        else: return self.Search(x,Root.left)
            
    def Delete(self,x):
        if self.root == None:return None
        node = self.Search(x)
        if node == None : return None
        else :
            print(node.pos)
            if node.left == None and node.right == None: self.DeleteLeaf(node)
            elif node.left == None or node.right == None : self.DeleteNodeWithOneChild(node)
            else : self.DeleteNodeWithTwoChild(node)
        
    def DeleteLeaf(self,currnode):
        parent = self.root
        while parent.left!=currnode and parent.right!=currnode:
            if currnode.data<parent.data: parent = parent.left
            else : parent = parent.right
        
        if parent.left == currnode : parent.left = None
        else : parent.right = None
        
    def DeleteNodeWithOneChild(self,node):
        if node.left != None :
            node.data = node.left.data
            node.left = None
        else :
            node.data = node.right.data
            node.right = None
            
    def DeleteNodeWithTwoChild(self,node):
        successor = node.right
        while successor.left != None : successor = successor.left
        node.data = successor.data
        if successor.right == None : self.DeleteLeaf(successor)
        else : self.DeleteNodeWithOneChild(successor)

try:
    Q = int(input())
    b = BST()
    for _ in range(Q):
        query = input().split()
        x = int(query[1])
        if query[0]== 'i':
            b.Insert(x)
        else :
            b.Delete(x)
except:
    pass
            
            
        
