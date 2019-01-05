'''
TLB Error
 n=int(input())
        sidelen=deque(map(int,input().split()))
        answer='Yes'
        while len(sidelen)>0:
            largestlen=max(sidelen)
            #print(largestlen)
            if len(sidelen)==1:
                item=sidelen.pop()
            else:
                if largestlen not in (sidelen[0], sidelen[-1]):
                    answer='No'
                    break
                elif sidelen[0]>=sidelen[-1]:
                    item=sidelen.popleft()
                else:
                    item=sidelen.pop()
            if item<largestlen:
                answer='No'
                break
            #print(sidelen)
        print(answer)
'''
if __name__=='__main__':
    T=int(input())
    for i in range(T):
        n=int(input())
        sidelen=list(map(int,input().split()))
        l=len(sidelen)
        i=0
        while i<l-1 and sidelen[i]>=sidelen[i+1]:
            i+=1
        while i<l-1 and sidelen[i]<=sidelen[i+1]:
            i+=1
        if i==l-1:
            print('Yes')
        else:
            print('No')
