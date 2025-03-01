//
// Created by Irene Lu on 2025/1/6.
//
#include <iostream>
using namespace std;
#include <vector>
#include <set>

int longestConsecutive(vector<int>& nums) {
    set<int> my_set;

    for (int i=0;i<nums.size();i++)
    {
        my_set.insert(nums[i]);
    }
    int sum;
    if(nums.size()>0)sum=1;
    else sum=0;
    
    for(auto it=my_set.begin();it!=my_set.end();it++)
    {

        if(my_set.count(*it-1))
        {
            sum++;
        }
    }
    return sum;
}


int main()
{
    vector<int> nums={0,0,-1};
    cout<<longestConsecutive(nums);
    return 0;
}
