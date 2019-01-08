class Node:
    def __init__(self,value):
        '''
        Objective          : To create a node.
        Input parameters   :
        self(Implicit parameter)-> Object of type node.
                           value-> value of node.
        Output             : Node with data part equal to value and a link to the next node.
        '''
        self.data=value
        self.next=None

class LinkedList:
    def __init__(self):
        '''
        Objective          : To initialize the head pointer.
        Input parameters   :
        self(Implicit parameter)-> Object of type node.
        Output             : None
        '''
        self.head=None

    def InsertAtBeginning(self,value):
        '''
        Objective          : To insert a node at the beginning of a linked list.
        Input parameters   :
        self(Implicit parameter)-> Object of type node.
                           value-> value of node to be inserted.
        Output             : Linked list with new node at the beginning.
        '''
        if self.head==None:
            node=Node(value)
            self.head=node
        else:
            node=Node(value)
            node.next=self.head
            self.head=node

    def DeleteNode(self,value):
        '''
        Objective          : To delete a node with data part equal to value.
        Input parameters   :
        self(Implicit parameter)-> Object of type node.
                           value-> value of node to be deleted.
        Output             : Node if it is in the linked list otherwise None.
        '''
        p=self.head
        if p==None:
            print('Error !! List is Empty.')
            return  
        if p.data==value:
            self.head=p.next
            return p.data

        while p!=None:
            if p.data==value:
                r=self.head
                while r.next!=p:
                    r=r.next
                r.next=p.next
                return p.data
            else:
                p=p.next
        
        return None
                
        

    def __str__(self):
        '''
        Objective          : To return string representation of linked list.
        Input parameters   :
        self(Implicit parameter)-> Object of type node.
        Output             : Linked list
        '''
        l=[]
        p=self.head
        if p==None:
            return "List is Empty."
        while p!=None:
            l.append(p.data)
            p=p.next

        return ' --> '.join(str(x) for x in l)

def main():
    print('*************************************************LINKED LIST*****************************************')
    print('1. Create and Insert a node at beginning  \n2. Delete a node \n3. Display linked list \n4. Exit')
    flag=True
    l=LinkedList()
    while flag==True:
        ch=int(input('Enter the choice 1/2/3/4 :'))
        if ch==1:
            node=int(input('Enter node to be inserted :'))
            l.InsertAtBeginning(node)

        elif ch==2:
            node=int(input('Enter node to be deleted :'))
            print(l.DeleteNode(node))
        
        elif ch==3:
            print(l)

        elif ch==4:
            flag=False

        else:
            print('ERROR!!! Wrong Choice.')
    
    

if __name__=='__main__':
    main()
    



        
        
        
    
