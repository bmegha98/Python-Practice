def merge_the_tools(string, k):
    i=len(string)//k
    j=0
    for tmp in range(i):
        m=[]
        for ch in string[j:j+k]:
            if ch not in m:
                m.append(ch)
        print(''.join(m))
        j+=k
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
