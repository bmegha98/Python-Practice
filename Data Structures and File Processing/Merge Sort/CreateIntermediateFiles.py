import pickle,time
blocksize=1000
def RecordKey(record):
    '''
    Objective        : To return key of the given node.
    Input Parameters :
                 record-> Object of type Record.
    Output           : Key of the given node.
    '''
    return record.key

def CreateIntermediateFiles(filename,file1,file2):
    '''
    Objective        : To create files f1 and f2.
    Input Parameters :
            blocksize-> Number of records to be sorted at a time.
             filename-> filename from which intermediate files are to be created.
    Output           : None
    '''
    global blocksize
    start=time.time()
    f1=open(file1,'wb')
    f2=open(file2,'wb')
    f=open(filename,'rb')
    flag=True
    while flag:
        lst1,lst2=[],[]
        try:
            for _ in range(blocksize):
                lst1.append(pickle.load(f))
        except EOFError:flag=False
        lst1.sort(key=RecordKey)
        for ele in lst1:
            pickle.dump(ele,f1)

        try:
            for _ in range(blocksize):
                lst2.append(pickle.load(f))
        except EOFError:flag=False
        lst2.sort(key=RecordKey)
        for ch in lst2:pickle.dump(ch,f2)      
        
    f.close(),f1.close(),f2.close()
    end=time.time()
    print('Time taken to create intermediate files : ',end-start,'sec.')

    
                                 
                        

    
