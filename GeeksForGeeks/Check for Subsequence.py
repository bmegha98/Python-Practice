'''
Given two strings A and B, find if A is a subsequence of B.
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        strings = list(input().split())
        subseq , string = strings[0],strings[1]
        j = 0
        flag = 0
        while j < len(subseq):
            i = string.find(subseq[j])
            if i == -1:
                flag = 1
                break
            string = string[i+1:]
            j+=1
        if flag == 1 : print(0)
        else : print(1)
