'''
We have N persons sitting on a round table. Any person can do a handshake with any other person.In how many ways these N people can make 
handshakes so that no two handshakes crosses each other. N would be even. 
'''

def Catalan(n): 
    catalan = [1 for i in range(n + 1)] 
    
    for i in range(2, n + 1): 
        catalan[i] = 0
        for j in range(i): 
            catalan[i] += (catalan[j] *catalan[i - j - 1]) 
      
    return catalan[n] 
    
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(Catalan(N//2))
