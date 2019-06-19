'''
Given an array of words, print the count of all anagrams together in sorted order (increasing order of counts).
For example, if the given array is {“cat”, “dog”, “tac”, “god”, “act”}, then grouped anagrams are “(dog, god) (cat, tac, act)”. So the
output will be 2 3.
Single line output, print the counts of anagrams in increasing order.
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(input().split())
        temp = [''.join(sorted(x)) for x in A]
        d = dict()
        for ch in temp:
            if ch not in d:d[ch]=1
            else:d[ch]+=1
        print(*sorted(d.values()))
