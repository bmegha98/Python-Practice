def average(array):
    l=set(array)
    avg=sum(l)/len(l)
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
