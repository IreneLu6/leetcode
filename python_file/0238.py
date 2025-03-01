
from typing import List

def productExceptSelf( nums: List[int]) -> List[int]:
    n_len=len(nums)
    answer=[0]*n_len
    answer[0]=1
    for i in range (1,n_len):
        answer[i]=nums[i-1]*answer[i-1]

    R=1
    for i in range(n_len-1,0,-1):
        answer[i]=R*answer[i]
        R*=nums[i]
    return answer


nums=[1,2,3,4]
productExceptSelf(nums)
