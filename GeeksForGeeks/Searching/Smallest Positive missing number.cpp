/*
You are given an array arr[] of N integers including 0. The task is to find the smallest positive number missing from the array.
Note: Expected solution in O(n) time using constant extra space.
Single line output, print the smallest positive number missing.
*/

#include<iostream>
using namespace std;
int main()
 {
	int T ;
	cin>>T;
	for(int i=0;i<T;i++)
	{
	    int N;
	    cin>>N;
	    int A[N]={0};
	    
	    for(int j=0;j<N;j++)
	    {
	        int x;
	        cin>>x;
	        if(x>0 && x<= N)
	        {
	            A[x-1] = -1;
	        }
	    }
	    for(int k=0;k<N;k++)
	    {
	        if(A[k]==0)
	        {
	            cout<<k+1<<endl;
	            break;
	        }
	    }
	}
	return 0;
