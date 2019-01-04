from collections import deque
if __name__=='__main__':
    N=int(input())
    d=deque()
    for i in range(N):
        operations=input().split()
        if operations[0]=='append':
            d.append(int(operations[1]))
        elif operations[0]=='pop':
            d.pop()
        elif operations[0]=='popleft':
            d.popleft()
        else:
            d.appendleft(int(operations[1]))
    print(' '.join(str(ch) for ch in d))
    
