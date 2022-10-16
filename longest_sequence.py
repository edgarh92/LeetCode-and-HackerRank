class Solution:
    def longestConsecutive(self,nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            start_of_sequence = n - 1

            if start_of_sequence not in numSet:
                length = 1
                next_value = n + 1
                while next_value in numSet:
                    next_value+=1
                    length+=1
                longest = max(length, longest)
        return longest