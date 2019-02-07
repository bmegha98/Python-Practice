'''
//C++ Program
#include<iostream>
using namespace std;
int main()
 {
	int t;
	cin>>t;
	for(int k=0;k<t;k++)
	{
	    int i,n;
	    cin>>n;
	    int a[n];
	    for(i=0;i<n;i++)
	    cin>>a[i];
	    i=0;
	    int j=n-1;
	    while(i<j)
	    {
	       
	        cout<<a[j]<<" ";
	        j--;
	        cout<<a[i]<<" ";
	        i++;
	        
	    }
	    if(i==j)
	    cout<<a[i];
	    cout<<endl;
	}
	return 0;
}
'''
if __name__=='__main__':
  T=int(input())
    for _ in range(T):
        N=int(input())
        A=list(map(int,input().split()))
        i=0
        j=N-1
        l=[]
        while i<j:
            l.extend([A[j],A[i]])
            j-=1
            i+=1
        if i==j:l.append(A[i])
        print(*l)
