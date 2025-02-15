#include <iostream>
#include <vector>
using namespace std;
int getquotient(int divisor,int dividend){
    int start=0;
    int end=dividend;
    int mid=start+(end-start)/2;
     int ans=0;
    while(start<=end){ 
        int product=mid*divisor;
        if (product==dividend)
        {
            return mid;
        }
        else if (product>dividend)
        {
            end=mid-1;
        }
        else{
            ans=mid;
            start=mid+1;
        }
       int mid=start+(end-start)/2; 
    }
    return ans;
}
int main()
{
    int res=getquotient(7,29);
    cout<<"The result is: "<<res;
}