from typing import List

def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    merge_in=[]
    intervals.sort()
    j=0
    merge_in.append(intervals[0])
    i_len=len(intervals)
    for i in range(i_len):
        if merge_in[j][1]>=intervals[i][0]:
            l=min(merge_in[j][0],intervals[i][0])
            r=max(merge_in[j][1],intervals[i][1]);
            merge_in.pop()
            merge_in.append([l,r])
        else :
            merge_in.append(intervals[i])
            j+=1
    return merge_in

