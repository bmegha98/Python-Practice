'''
Write a method to replace all the spaces in a string S with ‘%20’. You may assume that the string has sufficient space
(or allocated memory) at the end to hold the additional characters,

Note: The leading and trailing spaces should be trimmed off and not replaced by %20.
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        S = input()
        N = int(input())
        S = S.strip()
        S = S.replace(' ','%20')
        print(S)
