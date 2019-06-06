'''
arvis is weak in computing palindromes for Alphanumeric characters.
While Ironman is busy fighting Thanos, he needs to activate sonic punch but Jarvis is stuck in computing palindromes.
You are given a string S containing alphanumeric characters. Find out whether the string is a palindrome or not.
If you are unable to solve it then it may result in the death of Iron Man.

Note: Consider alphabets and numbers only for palindrome check. Ignore symbols and whitespaces.
Each new line of the output contains "YES" if the string is palindrome and "NO" if the string is not a palindrome.
'''
def Check(S,N):
    flag = 0
    i , j = 0 ,N-1
    while i<=j:
        if S[i]!=S[j]:
            flag = 1
            break
        i+=1
        j-=1
    if flag == 0 : print('YES')
    else : print('NO')
    
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        S = input()
        T = ''
        for ch in S :
            if ch.isalnum():
                T+=ch
                
        T = T.upper()
        Check(T,len(T))
