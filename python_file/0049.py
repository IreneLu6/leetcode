from typing import List
import collections
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    mp = collections.defaultdict(list)

    for st in strs:
        key = "".join(sorted(st))
        mp[key].append(st)

    return list(mp.values())


strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
groupAnagrams(strs)