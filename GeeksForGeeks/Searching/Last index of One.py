'''
Given a string S consisting only '0's and '1's,  print the last index of the '1' present in it.
Corresponding to every test case, output the last index of 1. If 1 is not present, print "-1" (without quotes).
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        S = input()
        index = []
        for i in range(len(S)):
            if S[i] == '1': index.append(i)
        if index !=[] : print(index[-1])
        else : print(-1)
