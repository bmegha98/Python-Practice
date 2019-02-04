'''
Given an array A of N elements. Find the majority element in the array. 
A majority element in an array A of size N is an element that appears more than N/2 times in the array.
'''
T=int(input())
for _ in range(T):
    flag=0
    N=int(input())
    A=list(map(int,input().split()))
    j,d=1,{}
    for i in range(N):
        ch=A[i]
        if ch not in d:
            d.update({ch:j})
        else:
            d[ch]+=1
    for k,val in d.items():
        if val>(N//2):
            print(k)
            flag=1
            break
    if flag==0:print('-1')
    
