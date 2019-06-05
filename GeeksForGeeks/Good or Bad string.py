'''
In this problem, a String S is composed of lowercase alphabets and wildcard characters i.e. '?'. Here, '?' can be replaced by any of the
lowercase alphabets. Now you have to classify the given String on the basis of following rules:

If there are more than 3 consonants together or more than 5 vowels together, the String is considered to be "BAD". A String is considered
"GOOD" only if it is not “BAD”.
'''
def vowel(char):
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        return True
    return False
    
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        s = input()
        conscount , vowcount = 0,0
        maxcons ,maxvow = 3 , 5
        bad = False
        
        for ch in s:
            if vowel(ch):
                conscount = 0
                vowcount+=1
                if vowcount > maxvow :
                    bad = True
                    break
            elif ch == '?':
                vowcount+=1
                conscount+=1
                if vowcount > maxvow or conscount > maxcons :
                    bad = True
                    break
            else:
                vowcount = 0
                conscount+=1
                if conscount > maxcons :
                    bad = True
                    break
        
        if bad:print(0)
        else : print(1)
