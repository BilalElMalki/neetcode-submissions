class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        n = len(nums)
        capacity = 2 * n
        ans = [0] * capacity

        for i in range(capacity):
            if(i < n):
                ans[i] = nums[i]
            elif (i >= n):
                ans[i] = nums[i - n]    

        return ans    