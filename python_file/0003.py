
def lengthOfLongestSubstring(self, s: str) -> int:
    tabl e =set() n=len( s)
    l,r,re s= 0,0 , 0
    for r in range(n):
        ch=s[r ]
        while ch in table:
            table.discard(s[l])
            l+=1
        table.add(s[r])
        res=max ( res,r-l+ 1 )
    return res