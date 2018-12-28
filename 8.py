def Average(StuDict,Student):
    s=0
    for i in StuDict:
        if i==Student:
            l=StuDict.get(i)
            break
    for ch in l:
        num=eval(ch)
        s+=num
    avg=s/len(l)
    avg="{:.2f}".format(avg)            #to round off upto 2 decimal places
    return avg

def main():
    StuDict={}
    N=int(input())
    for i in range(N):
        lst=[]
        IString=input()
        l=IString.split()
        k=l[0]
        lst.extend([l[1],l[2],l[3]])
        StuDict.update({k:lst})
    #print(StuDict)
    stu=input()
    avg=Average(StuDict,stu)
    print(avg)
if __name__=='__main__':
    main()
