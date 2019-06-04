'''
Given a string S, check if it is palindrome or not.
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = input()
        flag = 0
        i , j = 0 ,N-1
        while i<=j:
            if S[i]!=S[j]:
                flag = 1
                break
            i+=1
            j-=1
        if flag == 0 : print('Yes')
        else : print('No')
