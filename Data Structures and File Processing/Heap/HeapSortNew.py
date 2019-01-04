def HeapInsert(heap,e):
    if heap==[]:
        heap.append(e)
    else:
        heap.append(e)
        index=len(heap)-1
        while index>0:
            parent=(index-1)//2
            if e>heap[parent]:
                heap[index]=heap[parent]
                index=parent
            else:
                break
        heap[index]=e

def HeapDelete(heap):
    if heap==[]:
        return
    if len(heap)==1:
        heap.pop()
        return
    heap[0]=heap[-1]
    heap.pop()
    index=0
    val=heap[0]
    while index<len(heap):
        child1=2*index+1
        child2=2*index+2
        if child1>len(heap)-1 : break
        if child1<len(heap) and child2>=len(heap): maxchild=heap[child1]
        else : maxchild=max(heap[child1],heap[child2])
            
        if maxchild==heap[child1]:
            if maxchild>val:
                heap[index]=maxchild
                index=child1
            else:
                break
        else:
            if maxchild>val:
                heap[index]=maxchild
                index=child2
            else:
                break
            
    heap[index]=val
    
def HeapSort(lst):
    heap=[]
    SortedHeap=[]
    for i in lst:
        HeapInsert(heap,i)
    for i in range(len(heap)):
        SortedHeap.append(heap[0])
        HeapDelete(heap)
    return SortedHeap
    
def main():
    print('Enter list to be sorted :')
    l=list(map(int,input().split()))
    print('Sorted list is :')
    print(HeapSort(l))
    

if __name__=='__main__':
    main()
