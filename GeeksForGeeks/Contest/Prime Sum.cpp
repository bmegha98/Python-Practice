'''
Given a positive number N. The task is to find sum of all the primes upto N(inclusive).
'''
#include <bits/stdc++.h> 
using namespace std;
int sumOfPrimes(int n) 
{ 
    bool prime[n + 1]; 
    memset(prime, true, n + 1);
    for (int p = 2; p * p <= n; p++)
    {
        if (prime[p] == true) 
        { 
            for (int i = p * 2; i <= n; i += p) 
                prime[i] = false; 
        } 
    } 
    int sum = 0; 
    for (int i = 2; i <= n; i++) 
        if (prime[i]) 
            sum += i; 
    return sum; 
} 
int main()
 {
	int T;
	cin>>T;
	for(int i=0;i<T;i++)
	{
	    int N;
	    cin>>N;
	    cout<<sumOfPrimes(N)<<endl; 
	}
}
