class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        m=0
        for i in s:
            c=1
            if i-1 not in s:
                while i+1 in s:
                    c+=1
                    i+=1
            if m<c:
                m=c
        return m