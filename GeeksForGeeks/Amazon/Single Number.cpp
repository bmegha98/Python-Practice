/*
Given an array of positive integers where every element appears even times except for one. Find that number occuring odd number of times.
*/

#include<iostream>
using namespace std;
int main()
 {
	int t;
	cin>>t;
	while(t--)
	{
	    int n;
	    cin>>n;
	    int A[n];
	    int x = 0;
	    for(int i =0;i<n;i++)
	    {
	        cin>>A[i];
	        x = x^A[i];
	    }
	    
	    cout<<x<<endl;
	}
	return 0;
}
