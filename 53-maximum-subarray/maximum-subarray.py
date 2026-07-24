class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m=max(nums)
        sum=0
        for i in nums:
            if sum+i>i:
                sum=sum+i
            else:
                sum=i
            if m<sum:
                m=sum
        return m