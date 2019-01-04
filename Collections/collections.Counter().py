from collections import Counter
if __name__=='__main__':
    Tot_Money=0
    N=int(input())
    l=list(map(int,input().split()))
    Shoes=Counter(l)
    #print(Shoes)
    No_Cust=int(input())
    for i in range(No_Cust):
        Customer=list(map(int,input().split()))
        if Shoes[Customer[0]]!=0:
            Tot_Money+=Customer[1]
            Shoes[Customer[0]]-=1
    print(Tot_Money)
