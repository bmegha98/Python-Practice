import math
class Heap:
    heap=[]
    def __init__(self):
        '''
        Objective        : To initialize an empty heap.
        Input parameters :
                    self : Object of class Heap.
        Output           : None
        '''
        #Approach : Heap is an empty list.
        self.heap=[]
    def HeapInsert(self,e):
        '''
        Objective   : To insert an element in a heap.
        Input       :
               self : Object of class Heap.
                   e: Element to be inserted in the list.
        Output      : None
        Side Effect : Element is inserted at proper position.
        '''
        #Approach : Element is compared with its parent node and if it is larger then swap them and continue.
        if self.heap==[]:
            self.heap.append(e)
        else:
            self.heap.append(e)
            index=len(self.heap)-1
            while index>0:
                parent=math.floor((index-1)//2)
                if e>self.heap[parent]:
                    self.heap[index]=self.heap[parent]
                    index=parent
                else:
                    break
            self.heap[index]=e

    def HeapDelete(self):
        '''
        Objective   : To delete element at the root node of heap.
        Input       :
               self : Object of class Heap.
        Output      : None
        Side Effect : Element is removed from root node and remaining elements constitue heap.
        '''
        #Approach : Remove first element from heap and place the last element at its proper position in heap.
        self.heap[0]=self.heap[-1]
        self.heap.pop()
        index=0
        val=self.heap[0]
        while index<len(self.heap):
            child1=2*index+1
            child2=2*index+2
            if child1>len(self.heap)-1 : break
            if child1<len(self.heap) and child2>=len(self.heap): maxchild=self.heap[child1]
            else : maxchild=max(self.heap[child1],self.heap[child2])
                
            if maxchild==self.heap[child1]:
                if maxchild>val:
                    self.heap[index]=maxchild
                    index=child1
                else:
                    break
            else:
                if maxchild>val:
                    self.heap[index]=maxchild
                    index=child2
                else:
                    break
                
        self.heap[index]=val

    def __str__(self):
        '''
        Objective        : To print heap object.
        Input parameters :
                    self : Object of class Heap.
        Output           : string representation of heap object.
        '''
        #Approach : use print() function.
        return str(self.heap)
        
            
