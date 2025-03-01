from typing import List
import collections
def twoSum(nums: List[int], target: int) -> List[int]:
    hash=dict()
    for i,num in enumerate(nums):
        if(target-num) in hash:
           return [i,hash[target-num]]
        hash[num]=i
    return []


nums=[2,7,11,15]
twoSum(nums,9)