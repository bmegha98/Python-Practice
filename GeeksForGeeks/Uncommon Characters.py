'''
Find and print the uncommon characters of the two given strings S1 and S2. Here uncommon character means that either the character is 
present in one string or it is present in other string but not in both. The strings contains only lowercase characters and can contain
duplicates.
print the uncommon characters of the two given strings in sorted order.
'''
// One Method
'''
if __name__ =='__main__':
    T= int(input())
    for _ in range(T):
        s1 = input()
        s2 = input()
        set1 = set(s1)
        set2 = set(s2)
        res = set1.symmetric_difference(set2)
        res=list(res)
        res.sort()
        print(''.join(res))
'''
// Another Method
if __name__ =='__main__':
    T= int(input())
    for _ in range(T):
        s1 = input()
        s2 = input()
        res = []
        for ch in s1:
            if ch not in s2 and ch not in res:
                res.append(ch)
        
        for ch in s2:
            if ch not in s1 and ch not in res:
                res.append(ch)
        
        res.sort()
        print(''.join(res))
                
