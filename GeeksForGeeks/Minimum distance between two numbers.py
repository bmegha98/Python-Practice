'''
You are given an array A, of N elements. You need to find minimum distance between given two integers x and y.
'''
def minDist(arr, n, x, y):
    if (x not in arr) or (y not in arr):
        return -1
    else:
        dist=list()
        p1=[i for i,val in enumerate(arr) if val==x]
        p2=[i for i,val in enumerate(arr) if val==y]
        for i in p1:
            for j in p2:
                dist.append(abs(i-j))
        return min(dist)
