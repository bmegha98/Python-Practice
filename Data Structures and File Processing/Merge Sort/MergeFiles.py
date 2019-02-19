import pickle,os,time,CreateIntermediateFiles as C
def getEOF(f):
    '''
    Objective       : To return pointer at the end of a given file.
    Input Parameters:
                   f-> File Pointer
    Output          : Ending pointer of file.
    '''
    endOfFile = f.seek(0,2)
    f.seek(0)
    return endOfFile

def RecordKey(record):
    '''
    Objective        : To return key of the given node.
    Input Parameters :
                 record-> Object of type Record.
    Output           : Key of the given node.
    '''
    return record.key
    
def MergeFiles(filename,file1,file2):
    '''
    Objective        : To Merge elements in sorted order.
    Input Parameters :
            blocksize-> Number of elements to be clubbed together at a time.
             filename-> file whose records are to be sorted.
    Output           : None
            
    '''
    start=time.time()
    while True:
        f1=open(file1,'rb')
        f2=open(file2,'rb')
        f3=open('f3.bin','wb')
        f4=open('f4.bin','wb')
        cf1,cf2=0,0
        if f2.tell()==getEOF(f2):
            f1.close()
            os.remove(filename)
            os.rename(file1,filename)
            break
        flag=True
        pickle.load(f1)
        recordSize=f1.tell()
        f1.seek(0)
        check=C.blocksize
        while True:
            if flag:file=f3
            else:file=f4
            try:
                while cf1<(check) and cf2<(check):
                    f1.seek(recordSize*cf1),f2.seek(recordSize*cf2)
                    ob1=pickle.load(f1)
                    ob2=pickle.load(f2)
                    if RecordKey(ob1)<=RecordKey(ob2):
                        pickle.dump(ob1,file)
                        cf1+=1
                    else:
                        pickle.dump(ob2,file)
                        cf2+=1
                while cf1<check:
                    f1.seek(recordSize*cf1)
                    pickle.dump(pickle.load(f1),file)
                    cf1+=1
                while cf2<check:
                    f2.seek(recordSize*cf2)
                    pickle.dump(pickle.load(f2),file)
                    cf2+=1
                check+=C.blocksize
                if flag:flag=False
                else:flag=True
                
            except:
                EOF=getEOF(f1)
                f1.seek(recordSize*cf1)
                while f1.tell() < EOF:
                    pickle.dump(pickle.load(f1),file)  
                break
            
        f1.close(),f2.close(),f3.close(),f4.close()
        os.remove(file1),os.remove(file2)
        os.rename('f3.bin',file1),os.rename('f4.bin',file2)
        C.blocksize*=2
    end=time.time()
    print('Time taken to maerge files : ',end-start,'sec.')
        

                                 
                        

    
