# Given an unsorted array of integers, find the length of longest increasing subsequence.

# Example:

# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

import sys
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        l = len(nums)
        lis = [1]*l
        for i in range(1, l):
            for j in range(0, i):
                if nums[j] < nums[i] and lis[j] >= lis[i]:
                    lis[i] = lis[j] + 1
        return max(lis)
                