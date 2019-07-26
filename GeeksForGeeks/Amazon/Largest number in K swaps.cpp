'''
Given a number K and string S of digits denoting a positive integer, build the largest number possible by performing swap operations on 
the digits of S atmost K times.
'''

#include <bits/stdc++.h> 
using namespace std; 

void findMaximumNum(string str, int k, string& max) 
{
    if(k == 0) 
        return; 
  
    int n = str.length(); 
    for (int i = 0; i < n - 1; i++) 
    { 
        for (int j = i + 1; j < n; j++) 
        {
            if (str[i] < str[j]) 
            { 
                swap(str[i], str[j]); 
                if (str.compare(max) > 0) 
                    max = str;
                findMaximumNum(str, k - 1, max); 
                swap(str[i], str[j]); 
            } 
        } 
    } 
}

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int k;
        cin>>k;
        string str;
        cin>>str;
        string max = str; 
        findMaximumNum(str, k, max); 
        cout<<max<<endl;
    }
    return 0;
}
