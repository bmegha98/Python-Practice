from collections import Counter
if __name__=='__main__':
    K=int(input())
    '''
    //TLB Error
     x=input().split()
    for ch in x:
        if x.count(ch)!=K:
            print(ch)
            break
    '''
    RoomList=map(int,input().split())
    cnt=Counter(RoomList)
    for num,count in cnt.items():
        if count!=K:
            print(num)
            break
