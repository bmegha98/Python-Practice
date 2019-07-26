/*
Given a number N. Write a program to check whether every bit in the binary representation of the given number is set or not.
*/

#include<iostream>
using namespace std;

bool Check(int n)
{
    while(n > 0)
    {
        if(!(n & 1))
        return false;
        
        n = n>>1;
    }
    return true;
}
int main()
 {
	int t;
	cin>>t;
	while(t--)
	{
	    int n;
	    cin>>n;
	    if(Check(n))
	    cout<<"YES"<<endl;
	    else
	    cout<<"NO"<<endl;
	}
	return 0;
}
