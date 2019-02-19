import pickle,random,time
import CreateIntermediateFiles as C,MergeFiles as M
from RecordClass import Record
            
def RecordSave(filename):
    '''
    Objective        : To save records in a file.
    Input Parameters :
            filename-> file name where records are to be saved.
    Output           : None
    '''
    start=time.time()
    minrange,maxrange=1000000,6000000
    NOR,constant=5000000,5
    lst=[i for i in range(minrange,maxrange)]
    f=open(filename,'wb')
    keys=random.sample(range(minrange,maxrange),NOR)
    for key in keys:   
        others=str(key)*constant
        rec=Record(key,others)
        pickle.dump(rec,f)
    '''
    j,upper=0,NOR
    while j<NOR:
        index=random.randrange(0,upper)
        key=lst.pop(index)
        others=str(key)*constant
        rec=Record(key,others)
        pickle.dump(rec,f)
        upper-=1
        j+=1
    '''   
    f.close()
    end=time.time()
    print('Time taken to save records in file :',end-start,' sec.')

def RangeRecords(Filename,StartRec,EndRec):
    '''
    Objective       : To retrieve records in range StartRec to EndRec.
    Input Parameters:
            Filename-> Name of file from which records are to be retrieved.
            StartRec-> Starting Record Number.
            EndRec  -> Ending Record Number.
    Output          :  None
    '''
    try:
        f=open(Filename,'rb')
        p=pickle.load(f)
        size=f.tell()
        start=f.seek(size*(StartRec-1))
        end=f.seek(size*(EndRec-1))
        f.seek(start)
        while start<=end:
            print(pickle.load(f))
            start+=size
        f.close()
    except:
        print('ERROR!!! File is empty.')
        
    
if __name__=='__main__':
    filename=input('Enter file to be sorted : ')
    print('Enter intermediate file names :')
    f1,f2=input(),input()
    RecordSave(filename)
    C.CreateIntermediateFiles(filename,f1,f2)
    M.MergeFiles(filename,f1,f2)
    choice='Y'
    while choice=='Y' or choice=='y':
        filename=input('Enter file name from which records are to be retrieved ')
        s=int(input('Enter start record number : '))
        e=int(input('Enter end record number : '))
        RangeRecords(filename,s,e)
        choice=input('Do you want to continue?(Y/y) : ')
      
    
    
   
    
                                 
                        

    
