class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        newset = set(nums)
        for num in nums:
            if (num - 1 ) not in newset:
                length = 1
                while (num+length) in newset:
                    length += 1
                longest = max(longest,length)
            
        
        return longest