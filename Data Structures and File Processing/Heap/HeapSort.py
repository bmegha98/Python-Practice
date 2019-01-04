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

def BuildHeap(lst,i=0):
    heap=[]
    for j in range(i,len(lst)):
        HeapInsert(heap,lst[j])
    lst[i:]=heap
    return lst[0:i]+lst[i:]

def HeapSort(lst,i=0):
    if i==len(lst):
        lst.sort()
        print(lst)
        
    else:
        lst=BuildHeap(lst,i)
        HeapSort(lst,i+1)
    
    
    
def main():
    #lst=[22,22,12,16,18,7,11,8,15]
    heap=[]
    HeapInsert(heap,22)
    HeapInsert(heap,16)
    HeapInsert(heap,25)
    HeapInsert(heap,18)
    print(heap)
    HeapDelete(heap)
    print(heap)
    
 

if __name__=='__main__':
    main()
        
        
