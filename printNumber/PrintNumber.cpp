//print number from 1 to 10 using recursion in C++
#include<iostream>
using namespace std;

void printNumber(int n)
{   
   if(n>0)
   {   
      cout<<n<<" ";
      printNumber(n-1);
   }
}

int main()
{
   int n=10;
   cout<<"Numbers from 1 to "<<n<<" are: ";
   printNumber(n);
   return 0;
}