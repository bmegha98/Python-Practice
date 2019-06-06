'''
Given a string S and text T. Output the smallest window in the string S having all characters of the text T. 
Both the string S and text T contains lowercase english alphabets.
'''
'''
# TLE (Brute-Force TEchnique)
def Check (s,T):
    flag = True
    for i in range(len(T)):
        if s.find(T[i])== -1:
            flag = False
            break
    return flag
    
      
def substrings(S,T):
  l = len(S)
  final = []
  for i in range(l): 
      for j in range(i+1,l+1): 
          ch = S[i: j]
          if len(ch)>= len(T) and Check(ch,T):
              if final == []: final.append(ch)
              else:
                  if len(ch)< len(final[-1]):
                      final.pop()
                      final.append(ch)
  return final

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        S = input()
        T = input()
        sub = substrings(S,T)
        if sub!=[]:print(sub[0])
        else : print(-1)

'''
no_of_chars = 256
  
def findSubString(string, pat):  
  
    len1 = len(string)  
    len2 = len(pat)  
  
    if len1 < len2:  
        return -1  
  
    hash_pat = [0] * no_of_chars 
    hash_str = [0] * no_of_chars  
  
    for i in range(0, len2):  
        hash_pat[ord(pat[i])] += 1
  
    start, start_index, min_len = 0, -1, float('inf')  
  
    count = 0 # count of characters  
    for j in range(0, len1):  
        hash_str[ord(string[j])] += 1
 
        if (hash_pat[ord(string[j])] != 0 and
            hash_str[ord(string[j])] <= 
            hash_pat[ord(string[j])]):  
            count += 1
  
        # if all the characters are matched  
        if count == len2:  
            while (hash_str[ord(string[start])] > 
                   hash_pat[ord(string[start])] or
                   hash_pat[ord(string[start])] == 0):  
              
                if (hash_str[ord(string[start])] >  
                    hash_pat[ord(string[start])]):  
                    hash_str[ord(string[start])] -= 1
                start += 1
              
            # update window size  
            len_window = j - start + 1
            if min_len > len_window:  
              
                min_len = len_window  
                start_index = start  
  
    if start_index == -1: 
        return -1  
     
    return string[start_index : start_index + min_len]  
  
if __name__ == "__main__": 
    T = int(input())
    for _ in range(T):
        S = input()
        T = input()
        print(findSubString(S, T))  
