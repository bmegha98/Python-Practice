'''
Given an unsorted array of size N of positive integers. One number 'A' from set {1, 2, …N} is missing and one number 'B' occurs twice in 
array. Find these two numbers.
Note: If you find multiple answers then print the Smallest number found. Also, expected solution is O(n) time and constant extra space.
'''
import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main (String[] args) {
	Scanner sc=  new Scanner(System.in);
	int t= sc.nextInt();
	while(t--!=0)
	{
	    int n= sc.nextInt();
	    int a[] = new int[n+1];
	    for(int i=0;i<n;i++)
	    {
	        int b= sc.nextInt();
	        a[b]++;
	    }
	    int m =0;
	    int r=0;
	    for(int i=1;i<=n;i++)
	    {
	        if(m==0 && a[i]==0)
	        m=i;
	        if(r==0 && a[i]>1)
	        r=i;
	    }
	    System.out.println(r+" "+m);
	}
	
	}
}
