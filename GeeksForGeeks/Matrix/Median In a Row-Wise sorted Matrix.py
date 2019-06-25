'''
We are given a row wise sorted matrix of size r*c, we need to find the median of the matrix given. It is assumed that r*c is always odd.
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        [r,c] = [int(y) for y in input().split()]
        l = []
        while True:
            tmp = [int(x) for x in input().split()]
            l.extend(tmp)
            if len(l) == r*c : break
        
        l.sort()
        print(l[(r*c)//2])
