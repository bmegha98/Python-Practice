'''
Given two strings of lowercase alphabets and a value K, your task is to complete the given function which tells if  two strings are
K-anagrams of each other or not.
Two strings are called K-anagrams if both of the below conditions are true.
1. Both have same number of characters.
2. Two strings can become anagram by changing at most K characters in a string.
'''
'''
# First Method
from collections import Counter
def areKAnagrams(str1, str2, k):
    if len(str1) == len(str2):
        if sum((Counter(str1)-Counter(str2)).values()) <= k:
            return True
    
    return False
'''
# Second Method
def CountUncommon(str1,str2):
    count = 0
    for ch in str1:
        if ch not in str2:
            count+=1
    return count
    
def areKAnagrams(str1, str2, k):
    if len(str1) == len(str2):
        if CountUncommon(str1,str2) <= k:
            return True
    
    return False
