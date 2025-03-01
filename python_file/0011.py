from typing import List


def maxArea(height: List[int]) -> int:
    l,r=0,len(height)-1
    ans=0
    while l<r:
        area=(l-r)*(min(height[l],height[r]))
        ans=max(ans,area)
        if(height[l]<height[r]):
            l+=1
        else:
            r-=1
    return ans

