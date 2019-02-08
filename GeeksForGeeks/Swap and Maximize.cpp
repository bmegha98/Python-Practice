'''
Given an array of n elements. Consider array as circular array i.e element after an is a1. The task is to find maximum sum of the 
difference between consecutive elements with rearrangement of array element allowed 
i.e after rearrangement of element find |a1 – a2| + |a2 – a3| + …… + |an – 1– an| + |an – a1|.
'''
#include <bits/stdc++.h> 
using namespace std; 
int main()
 {
	int t;
	cin>>t;
	for(int m=0;m<t;m++)
	{
	  int n;
	  cin>>n;
	  int A[n];
	  for(int p=0;p<n;p++)
	  cin>>A[p];
	  sort(A, A+n);
	  int i=0,j=n-1,s=0;
	  while(i<j)
	  {
	      s+=A[j]-A[i];
	      i++;
	      if(i<j)
	      s+=A[j]-A[i];
	      j-=1;
	      
	  }
	  s+=A[i]-A[0];
	  cout<<s<<endl;
	}
	return 0;
}
