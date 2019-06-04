'''
Given two strings S1 and S2 in lowercase, the task is to make them anagram. The only allowed operation is to remove a character from any 
string. Find minimum number of characters to be deleted to make both the strings anagram. If two strings contains same data set in any
order then strings are called Anagrams.
'''
# function to calculate minimum numbers of characters to be removed to make two strings anagram.

def remAnagram(str1,str2):
    s = set(str1).union(set(str2))
    dict1 ,dict2 = {} , {}
    for ch in s :
        dict1[ch] = str1.count(ch)
    
    for ch in s :
         dict2[ch] = str2.count(ch)
    
    val1 = list(dict1.values())
    val2 = list(dict2.values())
    
    MinSum = 0
    for i in range(len(val1)):
        absolute = abs(val1[i]-val2[i])
        MinSum+=absolute
    
    return MinSum
